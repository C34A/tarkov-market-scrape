#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys

def main():
    link = "https://tarkov-market.com/item/Power_supply_unit"
    if len(sys.argv) > 1:
        link = sys.argv[1]

    page = requests.get(link).text
    psoup = BeautifulSoup(page, 'lxml')

    namefind = psoup.find('h1', {'class': 'title'})
    name = namefind.text

    valfind = psoup.find('div', {'class': 'price last'})
    valtext = valfind.text[:-1].strip().replace(',', '')
    value = float(valtext)

    print("item:", name)
    print("value:", str(value/1000) + 'k')

if __name__ == "__main__":
    main()