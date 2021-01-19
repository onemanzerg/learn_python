import requests
from bs4 import BeautifulSoup

url = 'https://www.banki.ru/products/currency/cash/ivanovo/'

sourse = requests.get(url)
mainText = sourse.text
soup = BeautifulSoup(mainText)

table = soup.find('table', {'class':'currency-table__table'})
usd = table.find('div', {'class':'currency-table__large-text'})
usd = usd.text

#eu = table.find('div', {'class':'currency-table__large-text'})
#eu = eu.text

#for tag in soup.findAll("currency-table__large-text"):
#        print("{0}: {1}".format(tag.name, tag.text))

print(usd)