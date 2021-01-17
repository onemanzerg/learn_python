import requests
from bs4 import BeautifulSoup

url = 'https://minfin.com.ua/currency/nbu/'

sourse = requests.get(url)
mainText = sourse.text
soup = BeautifulSoup(mainText)

table = soup.find('table', {'class':'table-auto'})
tr = table.find('td', {'class':'responsive-hide'})
tr = tr.text

print(tr)