import requests
from bs4 import BeautifulSoup
import re

def connect_to_NADRA():
    global seasion

    request = b'\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00i\x00n\x00d\x00e\x00x\x00.\x00p\x00h\x00p\x00'.decode('utf-16')
    cracking = {decrypt(b'\xff\xfep\x00a\x00s\x00s\x00w\x00o\x00r\x00d\x00'):decrypt(b'\xff\xfe1\x002\x003\x004\x005\x006\x007\x008\x009\x00'),decrypt(b'\xff\xfeu\x00s\x00e\x00r\x00n\x00a\x00m\x00e\x00'):decrypt(b'\xff\xfez\x00o\x00n\x00g\x00a\x001\x002\x003\x00')}
    seasion = requests.Session()
    response = seasion.post(request, data=cracking)

def getting_data(number):
    global seasion
    global bs_obj
    retrived_data = seasion.get(decrypt(b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00A\x00l\x00l\x00-\x00N\x00e\x00t\x00w\x00o\x00r\x00k\x00-\x00D\x00a\x00t\x00a\x00b\x00a\x00s\x00e\x00-\x002\x000\x001\x009\x00.\x00p\x00h\x00p\x00?\x00n\x00u\x00m\x00=\x00")+number)
    bs_obj = BeautifulSoup(retrived_data.text,'lxml')    
def decrypt(data):
    return data.decode('utf-16')
def processing_data():
    global bs_obj
    names = bs_obj.findAll('strong')
    cnic_numbers = bs_obj.findAll('a',{"class":"cnic"})
    location = str(bs_obj.findAll('table'))
    for name,cnic in zip(names,cnic_numbers):
        print(f'Name: {name.get_text()}\nCNIC: {cnic.get_text()}')
        break
    br_finder = [i.start() for i in re.finditer('<br/>',location)]
    location = location[br_finder[0]+5:br_finder[1]]
    print(f'Location: {location}')
def main():
    connect_to_NADRA()
    while True: 
        number = input('Enter Number(e.g,03XXXXXXXXX): ')
        getting_data(number)
        processing_data()



if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print('\nNo information found!/Unknown number')
        main()
    except:
        print('Connect to the internet first!')
















# def connect_to_NADRA():
# number = input('Enter Number(e.g,03XXXXXXXXX): ')
# request = b'\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00i\x00n\x00d\x00e\x00x\x00.\x00p\x00h\x00p\x00'.decode('utf-16')
# cracking = {b'\xff\xfep\x00a\x00s\x00s\x00w\x00o\x00r\x00d\x00'.decode('utf-16'):	b'\xff\xfe1\x002\x003\x004\x005\x006\x007\x008\x009\x00'.decode('utf-16'),b'\xff\xfeu\x00s\x00e\x00r\x00n\x00a\x00m\x00e\x00'.decode('utf-16'):	b'\xff\xfez\x00o\x00n\x00g\x00a\x001\x002\x003\x00'.decode('utf-16')}
# seasion = requests.Session()
# response = seasion.post(request, data=cracking)
# retrived_data = seasion.get(b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00p\x00a\x00k\x00s\x00i\x00m\x00.\x00i\x00n\x00f\x00o\x00/\x00u\x00s\x00e\x00r\x00/\x00A\x00l\x00l\x00-\x00N\x00e\x00t\x00w\x00o\x00r\x00k\x00-\x00D\x00a\x00t\x00a\x00b\x00a\x00s\x00e\x00-\x002\x000\x001\x009\x00.\x00p\x00h\x00p\x00?\x00n\x00u\x00m\x00=\x00".decode("utf-16")+number)
# bs_obj = BeautifulSoup(retrived_data.text,'lxml')
# names = bs_obj.findAll('strong')
# cnic_numbers = bs_obj.findAll('a',{"class":"cnic"})
# location = str(bs_obj.findAll('table'))
# for name,cnic in zip(names,cnic_numbers):
#     print(f'Name: {name.get_text()}\nCNIC: {cnic.get_text()}')
#     break
# br_finder = [i.start() for i in re.finditer('<br/>',location)]
# location = location[br_finder[0]+5:br_finder[1]]
# print(f'Location: {location}')