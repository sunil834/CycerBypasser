import os
import requests
import pyfiglet
import urllib.parse

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

# Clear the screen
clear_screen()

header = pyfiglet.figlet_format("\t\tCycerBypasser\t\t", font="standard")
print(header)
print('\t\t\t\t\thttps://github.com/sunil834/CycerBypasser')
print('\t\t\t\t\thttps://t.me/LuckyCrack3r')

def get_bypass_url(link):
    encoded_link = urllib.parse.quote(link)
    return f'https://dlr-api.woozym.workers.dev/api/deloreanv2/goatbypassersontop/free?url={encoded_link}'

while True:
    link = input('\n\nEnter your link or 0 to exit: ')
    if link == '0':
        print('Thank you!')
        break

    url = get_bypass_url(link)
    
    while True:
        try:
            src = requests.get(url)
        except requests.RequestException as e:
            print(f"\n\tError: Network error occurred: {e}\n")
            break

        if 'only supports' in src.text:
            print('\n\tError: Enter a valid URL to proceed!!!\t\n')
            break
        elif 'rb.gy/' in src.text:
            print('\n\tURL still in queue, retrying...\t\n')
            continue

        if src.status_code == 200:
            try:
                data = src.json()
                if 'result' in data:
                    print("\n\tResult: \n", data['result'])
                else:
                    print("\n\tError: Unexpected response format. Please try again.\n")
            except ValueError:
                print("\n\tError: Failed to parse JSON response.\n")
        else:
            print(f"\n\tError: Request failed with status code {src.status_code}.\n")
        break