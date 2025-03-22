from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import time
import random
import pyfiglet
import os
from colorama import init, Fore

# Initialize colorama
init()

# Define colors for output
r = Fore.RED
g = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE 
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, g, w, ye, cy]

info = g + '[' + w + 'INFO' + g + ']' + rs
attempt = g + '[' + w + 'ATTEMPT' + g + ']' + rs
sleep = g + '[' + w + 'SLEEP' + g + ']' + rs
error = g + '[' + r + 'ERROR' + g + ']' + rs

# Banner function
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('WinDy')
    print(random.choice(colors) + logo + rs)
    print(f'{info}{g} WinDy Adder {rs}')
    print(f'{info}{g} Telegram{rs}\n')

# Clear screen and show banner
def clscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

clscreen()
banner()

# Ensure script receives correct arguments
if len(sys.argv) < 7:
    print(f"{error} Not enough arguments provided! Expected 6 arguments, got {len(sys.argv) - 1}.")
    print("Usage: python addbyid.py <api_id> <api_hash> <phone> <file> <group> <scraped>")
    sys.exit(1)

# Read arguments from command line
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])
phone = str(sys.argv[3])
file = str(sys.argv[4])
group = str(sys.argv[5])
scraped = str(sys.argv[6])

# Debugging: Print received arguments
print(f"{info} Arguments received: api_id={api_id}, api_hash={api_hash}, phone={phone}, file={file}, group={group}, scraped={scraped}")

# Load users from CSV file
users = []
try:
    with open(file, 'r', encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=',', lineterminator='\n')
        next(rows, None)  # Skip header
        for row in rows:
            user = {
                'username': row[0],
                'id': int(row[1]),
                'access_hash': row[2],
                'group': row[3],
                'group_id': row[4]
            }
            users.append(user)
except FileNotFoundError:
    print(f"{error} The file '{file}' was not found!")
    sys.exit(1)
except Exception as e:
    print(f"{error} Error reading file '{file}': {e}")
    sys.exit(1)

# Connect to Telegram client
client = TelegramClient(phone, api_id, api_hash)
client.connect()
time.sleep(1.5)

# Get target group entity
try:
    target_group = client.get_entity(group)
    entity = InputPeerChannel(target_group.id, target_group.access_hash)
    group_name = target_group.title
    print(f"{info} Successfully retrieved group: {group_name}")
except Exception as e:
    print(f"{error} Error fetching group '{group}': {e}")
    sys.exit(1)

# Fetch scraped members
try:
    target_m = client.get_entity(scraped)
    client.get_participants(target_m, aggressive=True)
    print(f"{info} Retrieved members from scraped group.")
except Exception as e:
    print(f"{error} Failed to retrieve scraped members: {e}")
    sys.exit(1)

# Adding members
n = 0
added_users = []
print(f"{info} Adding members to {group_name}\n")

for user in users:
    n += 1
    if n % 50 == 0:
        print(f"{sleep} Sleeping 2 min to prevent possible account ban")
        time.sleep(120)

    try:
        print(user)
        added_users.append(user)
        user_to_add = client.get_entity(user['id'])
        client(InviteToChannelRequest(entity, [user_to_add]))
        us_id = user['id']
        print(f"{attempt} Adding {us_id}")
        print(f"{sleep} Sleeping 20s")
        time.sleep(20)

    except PeerFloodError:
        print(f"\n{error} Aborted. Peer Flood Error")
        break
    except UserPrivacyRestrictedError:
        print(f"{error} User Privacy Error (Skipped)")
        continue
    except ValueError:
        print(f"{error} Error in processing entity")
        continue
    except KeyboardInterrupt:
        print(f"{error} Aborted by user.")
        break
    except Exception as e:
        print(f"{error} Some other error occurred: {e}")
        continue

# Final cleanup
print(f"{info} {len(users)} attempts completed.")
os.remove(file)
sys.exit()
