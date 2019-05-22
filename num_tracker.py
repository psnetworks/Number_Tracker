import requests
from bs4 import BeautifulSoup
import re

def banner():
    '''This is tool's banner for looking cool'''

    print('''
db   db   j88D   .o88b. db   dD d8888b. d8888b.
88   88  j8~88  d8P  Y8 88 ,8P' VP  `8D 88  `8D
88ooo88 j8' 88  8P      88,8P     oooY' 88oobY'
88~~~88 V88888D 8b      88`8b     ~~~b. 88`8b
88   88     88  Y8b  d8 88 `88. db   8D 88 `88.
YP   YP     VP   `Y88P' YP   YD Y8888P' 88   YD
                      Copyright © 2019 Anonymous
    ''')
def decrypt(data):
    '''This function is use to decrypt data that is encrypt for some reasons.'''
    return data.decode('utf-16')

def is_num_valid(number):
    '''This function will check the number if it is correct or not.'''
    return True if re.findall('[0-9]{11,11}',number) and len(number) == 11 else False


def connect_to_NADRA():
    '''This function will connect to the database.'''
    request =	decrypt(b'\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00i\x00n\x00d\x00e\x00x\x00.\x00p\x00h\x00p\x00')
    cracking = {decrypt(b'\xff\xfep\x00a\x00s\x00s\x00w\x00o\x00r\x00d\x00'):decrypt(b'\xff\xfe1\x002\x003\x004\x005\x006\x007\x008\x009\x00'),decrypt(b'\xff\xfeu\x00s\x00e\x00r\x00n\x00a\x00m\x00e\x00'):decrypt(b'\xff\xfez\x00o\x00n\x00g\x00a\x001\x002\x003\x00')}
    session = requests.Session()
    session.post(request, data=cracking)
    return session

def gathered_data(session, number):
    '''This function is to get the information from the database about the number.'''
    retrived_data = session.get(decrypt(b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00A\x00l\x00l\x00-\x00N\x00e\x00t\x00w\x00o\x00r\x00k\x00-\x00D\x00a\x00t\x00a\x00b\x00a\x00s\x00e\x00-\x002\x000\x001\x009\x00.\x00p\x00h\x00p\x00?\x00n\x00u\x00m\x00=\x00")+number[1:])
    bs_obj = BeautifulSoup(retrived_data.text,'lxml')
    return bs_obj

def processed_data(data):
    '''Process and print the result gathered from the database.'''
    info = data.findAll('td')
    if info:
        try:
            from prettytable import PrettyTable
            data_table = PrettyTable()
            data_table.add_column('Type', [info[header_location].get_text()[:-2] for header_location in range(0,len(info),2)])
            data_table.add_column('Data', [info[data_location].get_text() for data_location in range(1,len(info),2)])
            print(data_table)
        except:
            #This portion will execute if someone don not have prettytable installed in its device
            print('*'*60)
            header_list = [info[header_location].get_text().strip() for header_location in range(0, len(info), 2)]
            data_list = [info[header_location].get_text() for header_location in range(1, len(info), 2)]
            for i, j in zip(header_list, data_list):
                print('{:<20}{}'.format(i,j))
            print('*' * 60)
    else:
        print('[-] No record found!')

def main():
    '''This is the main function where all dirty work will be happen.'''
    session = connect_to_NADRA()
    while True:
        number = input('Enter Number(e.g,03XXXXXXXXX): ')

        if is_num_valid(number):
            print('[+] Checking in our database...')
            data = gathered_data(session, number)
            processed_data(data)
        else:
            print('[-] Wrong syntext of number.please enter number in this formate 03XXXXXXXXX')

if __name__ == '__main__':
    # This is the main login of the this program.
    banner()
    print('[+] Loading Data from database...')
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] CTRL + C detected! Closing the program...')
    except:
        print('[-] Please check your internet connection!')
