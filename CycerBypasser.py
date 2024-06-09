import requests
import pyfiglet

header = pyfiglet.figlet_format("CycerBypasser", font="standard")
print(header)
print('\t\t\t\t\thttps://github.com/sunil834/CycerBypasser')
print('\t\t\t\t\thttps://t.me/LuckyCrack3r')

def get_bypass_url(link):
    return f'https://dlr-api.woozym.workers.dev/api/deloreanv2/goatbypassersontop/free?url={link}'

while True:
    link = input('\n\nEnter your link: ')
    url = get_bypass_url(link)
    src = requests.get(url)

    while True:
        if 'only supports' in src.text:
            print('\n\tError: Enter valid URL to proceed!!!\t\n')
            link = input('\n\nEnter your link: ')
            url = get_bypass_url(link)
            src = requests.get(url)
        elif 'rb.gy/' in src.text:
            print('\n\tURL still in queue, retrying...\t\n')
            src = requests.get(url)
        else:
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