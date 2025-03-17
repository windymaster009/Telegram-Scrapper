import csv
import sys
import pickle
import random
import os
import datetime
from colorama import init, Fore
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError, SessionPasswordNeededError
from telethon.tl.types import UserStatusRecently
from pyrogram import Client
from pyrogram.errors import FloodWait
import time

# Initialize Colorama
init()

lg = Fore.LIGHTGREEN_EX
rs = Fore.RESET
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN

info = lg + '[' + w + 'INFO' + lg + ']' + rs
error = lg + '[' + r + 'ERROR' + lg + ']' + rs
success = w + '[' + lg + 'SUCCESS' + w + ']' + rs
INPUT = lg + '[' + w + 'INPUT' + lg + ']' + rs

# Load accounts from vars.txt
try:
    with open('vars.txt', 'rb') as f:
        accs = []
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
except FileNotFoundError:
    print(f"{error}{r} vars.txt not found!{rs}")
    sys.exit()

# Select an account
print(f'{INPUT}{lg} Choose an account to scrape members:')
for i, acc in enumerate(accs):
    print(f'{lg}[{w}{i}{lg}] {acc}')
try:
    ind = int(input(f'{INPUT}{lg} Enter choice: '))
    api_id, api_hash, phone = accs[ind]
except (IndexError, ValueError):
    print(f"{error}{r} Invalid selection!{rs}")
    sys.exit()

# Connect to Pyrogram
pyro_client = Client("pyrogram_session", api_id=api_id, api_hash=api_hash, phone_number=phone)

# Connect to Telethon
telethon_client = TelegramClient(phone, api_id, api_hash)
telethon_client.connect()

# If not authorized, request login
if not telethon_client.is_user_authorized():
    try:
        telethon_client.send_code_request(phone)
        code = input(f'{INPUT}{lg} Enter the code for {phone}{r}: ')
        telethon_client.sign_in(phone, code)
    except SessionPasswordNeededError:
        password = input(f'{INPUT}{lg} Enter your 2FA password: {r}')
        telethon_client.sign_in(password=password)
    except PhoneNumberBannedError:
        print(f'{error}{r}{phone} is banned!{rs}')
        sys.exit()

# Get group info
username = input(f'{INPUT}{lg} Enter the exact username of the public group [Without @]: {r}')
target_grp = 't.me/' + str(username)
try:
    group = telethon_client.get_entity(target_grp)
except Exception as e:
    print(f"{error}{r} Failed to get group: {str(e)}{rs}")
    sys.exit()

print(f'{info}{lg} Scraping members from {rs}{group.title}')

# Scrape members using Pyrogram first
def scrape_with_pyrogram():
    members = []
    try:
        pyro_client.start()
        chat = pyro_client.get_chat(username)
        for member in pyro_client.get_chat_members(chat.id):
            members.append({
                'username': member.user.username if member.user.username else '',
                'user_id': member.user.id,
                'access_hash': '',
                'group': group.title,
                'group_id': group.id
            })
    except FloodWait as e:
        print(f"{error}{r} Pyrogram hit rate limit! Waiting {e.value} seconds...{rs}")
        time.sleep(e.value)
    except Exception as e:
        print(f"{error}{r} Pyrogram failed: {str(e)}{rs}")
    finally:
        pyro_client.stop()
    return members

# Scrape members using Telethon as a backup
def scrape_with_telethon():
    members = []
    try:
        all_members = telethon_client.get_participants(group, aggressive=True)
        for member in all_members:
            members.append({
                'username': member.username if member.username else '',
                'user_id': member.id,
                'access_hash': member.access_hash,
                'group': group.title,
                'group_id': group.id
            })
    except Exception as e:
        print(f"{error}{r} Telethon failed: {str(e)}{rs}")
    return members

# Start scraping with Pyrogram first
pyro_members = scrape_with_pyrogram()
print(f"{info}{lg} Pyrogram fetched {len(pyro_members)} members{rs}")

# If Pyrogram got too few members, use Telethon
if len(pyro_members) < 50:  # Adjust the threshold if needed
    print(f"{info}{lg} Pyrogram didn't fetch enough members, switching to Telethon...{rs}")
    telethon_members = scrape_with_telethon()
    print(f"{info}{lg} Telethon fetched {len(telethon_members)} members{rs}")
else:
    telethon_members = []

# Combine results, removing duplicates
all_members = {m['user_id']: m for m in (pyro_members + telethon_members)}.values()

# Save to CSV
print(f'{info}{lg} Saving members to members.csv...{rs}')
with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
    for member in all_members:
        writer.writerow([member['username'], member['user_id'], member['access_hash'], member['group'], member['group_id']])

print(f'{success}{lg} Scraping completed! {len(all_members)} members saved.{rs}')
