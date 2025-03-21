from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.channels import JoinChannelRequest
import csv
import time
import keyboard
import random
import pyfiglet
from colorama import init, Fore
import os
import pickle
import traceback
try:
    import beepy
except ImportError:
    if os.name == 'nt':
        os.system('pip install beepy')
    else:
        pass

init()

r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN 
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'INFO' + lg + ']' + rs
error = lg + '[' + r + 'ERROR' + lg + ']' + rs
success = w + '[' + lg + 'SUCCESS' + w + ']' + rs
INPUT = lg + '[' + w + 'INPUT' + lg + ']' + rs
plus = lg + '[' + w + '+' + lg + ']' + rs
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('WinDy')
    print(random.choice(colors) + logo + rs)
    print(f'{info}{lg} TG | TG - Adder{rs}')


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

with open('target_grp.txt', 'r') as f:
    scraped_grp = f.readline()
f.close()

clr()
banner()
users = []
input_file = 'members.csv'
with open(input_file, 'r', encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=',', lineterminator='\n')
    next(reader, None)
    for row in reader:
        user = {}
        user['username'] = row[0]
        user['user_id'] = row[1]
        user['access_hash'] = row[2]
        user['group'] = row[3]
        user['group_id'] = row[4]
        users.append(user)
accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break
print('\n' + info + lg + ' Creating sessions for all accounts...' + rs)
for a in accounts:
    iD = int(a[0])
    Hash = str(a[1])
    phn = str(a[2])
    clnt = TelegramClient(phn, iD, Hash)
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            code = input(f'{INPUT}{lg} Enter code for {phn}[s to skip]:{r}')
            if 's' in code:
                accounts.remove(a)
            else:
                clnt.sign_in(phn, code)
        except PhoneNumberBannedError:
            print(f'{error}{r}{phn} is banned!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print('\n'+info+lg+'Banned account removed'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print('\n'+info+' Sessions created!')
time.sleep(2)
print(f'{plus}{lg} Enter EXACT username of the public group[Without @]')
g = input(f'{plus}{lg} Username[Eg: Techmedies_Hub]: {r}')
group = 't.me/' + str(g)
print('\n')
print(f'{info}{lg} Joining from all accounts...{rs}\n')
for account in accounts:
    api_id = int(account[0])
    api_hash = str(account[1])
    phone = str(account[2])
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    username = client.get_entity(group)
    try:
        client(JoinChannelRequest(username))
        print(f'{success}{lg} Joined from {phone}')
    except:
        print(f'{error}{r} Error in joining from {phone}')
        accounts.remove(account)
    client.disconnect()
time.sleep(2)
clr()
number = len(accounts)
print(f'{info}{lg} Total accounts: {number}')
print(f'{info}{lg} If you have more than 10 accounts then it is recommended to use 10 at a time')
a = int(input(f'{plus}{lg} Enter number of accounts to use: {r}'))
to_use = []
print(f'\n{info}{lg} Distributing CSV files...{rs}')
time.sleep(2)
for i in accounts[:a]:
    done = []
    to_use.append(i)
    file = 'members' + str(accounts.index(i)) + '.csv'
    with open(file, 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
        for user in users[:50]:
            writer.writerow([user['username'], user['user_id'], user['access_hash'], user['group'], user['group_id']])
            done.append(user)
    f.close()
    del_count = 0
    while del_count != len(done):
        del users[0]
        del_count += 1
    if len(users) == 0:
        break
if not len(users) == 0:
    with open('members.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
        for user in users:
            writer.writerow([user['username'], user['user_id'], user['access_hash'], user['group'], user['group_id']])
    f.close()
    m = str(len(users))
    print(f'{info}{lg} Remaining {m} users stored in members.csv')
for acc in to_use:
    accounts.remove(acc)
with open('vars.txt', 'wb') as f:
    for acc in accounts:
        pickle.dump(acc, f)
    for k in to_use:
        pickle.dump(k, f)
    f.close()
with open('resume.txt', 'w') as f:
    f.write(scraped_grp)
    f.close()
print(f'{info}{lg} CSV file distribution complete{rs}')
time.sleep(2)
clr()
if not os.name == 'nt':
    print(f'{error}{r} Automation supports only Windows systems')
    sys.exit()
choice = int(input(f'{plus}{lg} Enter 1 to add by username or 2 to add by id: {r}'))
if choice == 1:
    program = 'usradder.py'
else:
    program = 'addbyid.py'
o = str(len(to_use))
print(f'\n{info}{r} This will be fully automated. Your PC mustn\'t be too laggy!')
print(f'{info}{r} Don\'t touch the keyboard and mouse until you hear an alert sound')
print(f'{info}{r} If you don\'t have speakers, wait until cmd window pop-up stops{rs}')
input(f'\n{plus}{lg} Press enter to continue...{rs}')
print(f'\n{info}{lg} Launching from {o} accounts...{rs}\n')
for i in range(5, 0, -1):
    print(random.choice(colors) + str(i) + rs)
    time.sleep(1)
for account in to_use:
    api_id = str(account[0])
    api_hash = str(account[1])
    phone = str(account[2])
    file = 'members' + str(to_use.index(account)) + '.csv'
    os.system('start cmd')
    time.sleep(1.5)
    keyboard.write('python' + ' ' + program + ' ' + api_id + ' ' + api_hash + ' ' + phone + ' ' + file + ' ' + group + ' ' + str(scraped_grp))
    keyboard.press_and_release('Enter')
    print(f'{success}{lg} Launched from {phone}')
beepy.beep(sound='ping')