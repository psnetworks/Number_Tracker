import requests
from bs4 import BeautifulSoup
import re
import subprocess
def banner():
    print('''\033[1;32;48m
db   db   j88D   .o88b. db   dD d8888b. d8888b.
88   88  j8~88  d8P  Y8 88 ,8P' VP  `8D 88  `8D
88ooo88 j8' 88  8P      88,8P     oooY' 88oobY'
88~~~88 V88888D 8b      88`8b     ~~~b. 88`8b
88   88     88  Y8b  d8 88 `88. db   8D 88 `88.
YP   YP     VP   `Y88P' YP   YD Y8888P' 88   YD
                      \033[1;31;48mCopyright © 2019 Anonymous
    ''')
def connect_to_NADRA():
    global seasion
    request =	decrypt(b'\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00i\x00n\x00d\x00e\x00x\x00.\x00p\x00h\x00p\x00')
    cracking = {decrypt(b'\xff\xfep\x00a\x00s\x00s\x00w\x00o\x00r\x00d\x00'):decrypt(b'\xff\xfe1\x002\x003\x004\x005\x006\x007\x008\x009\x00'),decrypt(b'\xff\xfeu\x00s\x00e\x00r\x00n\x00a\x00m\x00e\x00'):decrypt(b'\xff\xfez\x00o\x00n\x00g\x00a\x001\x002\x003\x00')}
    seasion = requests.Session()
    response = seasion.post(request, data=cracking)

def getting_data(number):
    global seasion
    global bs_obj
    retrived_data = seasion.get(decrypt(b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00A\x00l\x00l\x00-\x00N\x00e\x00t\x00w\x00o\x00r\x00k\x00-\x00D\x00a\x00t\x00a\x00b\x00a\x00s\x00e\x00-\x002\x000\x001\x009\x00.\x00p\x00h\x00p\x00?\x00n\x00u\x00m\x00=\x00")+number[1:])
    bs_obj = BeautifulSoup(retrived_data.text,'lxml')
def processing_data():
    global bs_obj
    info = bs_obj.findAll('td')
    print(f'\033[1;33;48m{info[0].get_text()}  {info[1].get_text()}')            #Number
    print(f'\033[1;33;48m{info[2].get_text()}    {info[3].get_text()}')          #Date
    print(f'\033[1;33;48m{info[4].get_text()}    {info[5].get_text()}')          #Name
    print(f'\033[1;33;48m{info[6].get_text()} {info[7].get_text()}')             #Address
    print(f'\033[1;33;48m{info[8].get_text()}    {info[9].get_text()}')          #City
    print(f'\033[1;33;48m{info[10].get_text()}    {info[11].get_text()}')        #Cnic

def decrypt(data):
    return data.decode('utf-16')

def is_num_valid(number):
    return True if re.findall('[0-9]{11,11}',number) else False

def main():
    try:
        subprocess.call('clear',shell=True)
    except:
        subprocess.call('cls',shell=True)

    banner()
    connect_to_NADRA()
    while True:
        number = input('\033[1;32;48mEnter Number(e.g,03XXXXXXXXX): ')
        if is_num_valid(number):
            print('[+] Checking in our database...')
            getting_data(number)
            processing_data()
        else:
            print('\033[1;31;48m[-] Wrong syntext of number.please enter number in this formate 03XXXXXXXXX')



if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print('\n\033[1;31;48m[-] No information found!')
        main()
    except:
        print('\033[1;31;48mConnect to the internet first!')
        main()
