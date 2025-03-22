# from telethon.sync import TelegramClient
# from telethon.tl.types import InputPeerChannel
# from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
# from telethon.tl.functions.channels import InviteToChannelRequest
# import sys
# import csv
# import time
# import random
# import pyfiglet
# #import traceback
# from colorama import init, Fore
# import os

# init()

# r = Fore.RED
# g = Fore.GREEN
# rs = Fore.RESET
# w = Fore.WHITE 
# cy = Fore.CYAN
# ye = Fore.YELLOW
# colors = [r, g, w, ye, cy]
# info = g + '[' + w + 'INFO' + g + ']' + rs
# attempt = g + '[' + w + 'ATTEMPT' + g + ']' + rs
# sleep = g + '[' + w + 'SLEEP' + g + ']' + rs
# error = g + '[' + r + 'ERROR' + g + ']' + rs
# def banner():
#     f = pyfiglet.Figlet(font='slant')
#     logo = f.renderText('WinDy')
#     print(random.choice(colors) + logo + rs)
#     print(f'{info}{g} TG Adder V2.1 by Windy{rs}')
#     print(f'{info}{g} Telegram - Scraper{rs}\n')

# def clscreen():
#     os.system('cls')

# clscreen()
# banner()
# api_id = int(sys.argv[1])
# api_hash = str(sys.argv[2])
# phone = str(sys.argv[3])
# file = str(sys.argv[4])
# group = str(sys.argv[5])
# class Relog:
#     def __init__(self, lst, filename):
#         self.lst = lst
#         self.filename = filename
#     def start(self):
#         with open(self.filename, 'w', encoding='UTF-8') as f:
#             writer = csv.writer(f, delimiter=",", lineterminator="\n")
#             writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
#             for user in self.lst:
#                 writer.writerow([user['username'], user['user_id'], user['access_hash'], user['group'], user['group_id']])
#             f.close()
# def update_list(lst, temp_lst):
#     count = 0
#     while count != len(temp_lst):
#         del lst[0]
#         count += 1
#     return lst
# users = []
# with open(file, encoding='UTF-8') as f:
#     rows = csv.reader(f, delimiter=',', lineterminator='\n')
#     next(rows, None)
#     for row in rows:
#         user = {}
#         user['username'] = row[0]
#         user['user_id'] = row[1]
#         user['access_hash'] = row[2]
#         user['group'] = row[3]
#         user['group_id'] = row[4]
#         users.append(user)
# client = TelegramClient(phone, api_id, api_hash)
# client.connect()
# time.sleep(1.5)
# target_group = client.get_entity(group)
# entity = InputPeerChannel(target_group.id, target_group.access_hash)
# group_name = target_group.title
# print(f'{info}{g} Adding members to {group_name}{rs}\n')
# n = 0
# added_users = []
# for user in users:
#     n += 1
#     added_users.append(user)
#     if n % 50 == 0:
#         print(f'{sleep}{g} Sleep 2 min to prevent possible account ban{rs}')
#         time.sleep(120)
#     try:
#         if user['username'] == "":
#             continue
#         user_to_add = client.get_input_entity(user['username'])
#         client(InviteToChannelRequest(entity, [user_to_add]))
#         usr_id = user['user_id']
#         print(f'{attempt}{g} Adding {usr_id}{rs}')
#         print(f'{sleep}{g} Sleep 20s{rs}')
#         time.sleep(20)
#     except PeerFloodError:
#         #time.sleep()
#         os.system(f'del {file}')
#         sys.exit(f'\n{error}{r} Aborted. Peer Flood Error{rs}')
#     except UserPrivacyRestrictedError:
#         print(f'{error}{r} User Privacy Error[non-serious]{rs}')
#         continue
#     except KeyboardInterrupt:
#         print(f'{error}{r} Aborted. Keyboard Interrupt{rs}')
#         update_list(users, added_users)
#         if not len(users) == 0:
#             print(f'{info}{g} Remaining users logged to {file}')
#             logger = Relog(users, file)
#             logger.start()
#     except:
#         print(f'{error}{r} Some Other error in adding{rs}')
#         continue
# os.system(f'del {file}')
# input(f'{info}{g}Adding complete...Press enter to exit...')
# sys.exit()


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

init()

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

def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('WinDy')
    print(random.choice(colors) + logo + rs)
    print(f'{info}{g} TG Adder V2.1 by Windy{rs}')
    print(f'{info}{g} Telegram - Scraper{rs}\n')

def clscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

clscreen()
banner()

# Ensure correct number of arguments
if len(sys.argv) < 6:
    sys.exit(f'{error} Not enough arguments provided! Expected 6 arguments, got {len(sys.argv) - 1}.\n'
             f'Usage: python addbyid.py <api_id> <api_hash> <phone> <file> <group>')

api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])
phone = str(sys.argv[3])
file = str(sys.argv[4])
group = str(sys.argv[5])

class Relog:
    def __init__(self, lst, filename):
        self.lst = lst
        self.filename = filename

    def start(self):
        with open(self.filename, 'w', encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
            for user in self.lst:
                writer.writerow([user['username'], user['user_id'], user['access_hash'], user['group'], user['group_id']])
        print(f'{info} Remaining users logged to {self.filename}')

def update_list(lst, temp_lst):
    count = 0
    while count != len(temp_lst):
        del lst[0]
        count += 1
    return lst

# Load members from CSV file
users = []
with open(file, encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=',', lineterminator='\n')
    next(rows, None)  # Skip header row
    for row in rows:
        user = {
            'username': row[0].strip(),
            'user_id': row[1].strip(),
            'access_hash': row[2].strip(),
            'group': row[3].strip(),
            'group_id': row[4].strip()
        }
        users.append(user)

# Connect to Telegram Client
client = TelegramClient(phone, api_id, api_hash)
client.connect()
time.sleep(1.5)

# Get target group details
target_group = client.get_entity(group)
entity = InputPeerChannel(target_group.id, target_group.access_hash)
group_name = target_group.title
print(f'{info}{g} Adding members to {group_name}{rs}\n')

n = 0
added_users = []

for user in users:
    n += 1
    added_users.append(user)

    if n % 50 == 0:
        print(f'{sleep}{g} Sleep 2 min to prevent possible account ban{rs}')
        time.sleep(120)

    try:
        # Handle cases where username is empty
        if not user['username']:
            user_to_add = client.get_input_entity(int(user['user_id']))
            display_name = f"User ID: {user['user_id']}"
        else:
            user_to_add = client.get_input_entity(user['username'])
            display_name = f"{user['username']} (User ID: {user['user_id']})"

        # Attempt to add the user
        client(InviteToChannelRequest(entity, [user_to_add]))
        print(f'{attempt}{g} Adding {display_name}{rs}')
        print(f'{sleep}{g} Sleep 20s{rs}')
        time.sleep(20)

    except PeerFloodError:
        os.system(f'del {file}' if os.name == 'nt' else f'rm {file}')
        sys.exit(f'\n{error}{r} Aborted. Peer Flood Error{rs}')

    except UserPrivacyRestrictedError:
        print(f'{error}{r} User Privacy Error[non-serious]{rs}')
        continue

    except KeyboardInterrupt:
        print(f'{error}{r} Aborted. Keyboard Interrupt{rs}')
        update_list(users, added_users)
        if users:
            logger = Relog(users, file)
            logger.start()
        sys.exit()

    except Exception as e:
        print(f'{error}{r} Some Other error in adding: {str(e)}{rs}')
        continue

os.system(f'del {file}' if os.name == 'nt' else f'rm {file}')
input(f'{info}{g}Adding complete... Press enter to exit...')
sys.exit()
