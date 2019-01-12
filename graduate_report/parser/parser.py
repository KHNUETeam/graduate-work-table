import requests
from bs4 import BeautifulSoup

count = 20

url = 'http://irbis-nbuv.gov.ua/cgi-bin/irbis64r_81/cgiirbis_64.exe'
responce = requests.get('http://irbis-nbuv.gov.ua/cgi-bin/irbis64r_81/cgiirbis_64.exe?C21COM=F&I21DBN=ARD_EX&P21DBN=ARD&S21FMT=&S21ALL=&Z21ID=')

data = {
    'I21DBN':'ARD',
    'P21DBN':'ARD',
    'S21REF':10,
    'S21CNR': count,
    'S21STN': 1,
    '2_S21P02': 1,
    '2_S21P03': 'K=',
    '2_S21P05': 'Ключевые слова',
    '2_S21STR': 'формування механізму',
    '2_S21LOG': 0,
    '2_S21P01': 3,
    '1_S21P01': 2,
    '1_S21P03': 'RZN=',
    '1_S21P05': 'Тематика поиска',
    '1_S21STR': '',
    '4_S21P01': 2,
    '4_S21P03': 'KNS=',
    '4_S21P05': 'Спеціальність ВАК',
    '4_S21STR': '',
    '3_S21P01': 0,
    '3_S21P02': 1,
    '3_S21P03': 'A=',
    '3_S21P05': 'Автор',
    '3_S21STR': '',
    '5_S21P01': 2,
    '5_S21P03': 'G=',
    '5_S21P05': 'Год издания',
    '5_S21LOG': 5,
    '5_S21P06': 2000,
    '5_S21P07': 2002,
    'S21FMT': 'fullw',
    'C21COM': 'S',
    'C21COM1': 'Пошук'
}

responce = requests.post(url, data=data)

html = BeautifulSoup(responce.text, 'html.parser')
print(html.find_all('table', {'class':'advanced'})[4])
