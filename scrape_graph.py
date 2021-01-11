from database import database
from bs4 import BeautifulSoup
import requests
from typing import Tuple
from datetime import datetime
import time
import matplotlib.pyplot as plt


def scrape(link: str) -> Tuple[str, float]:
    page = requests.get(link).text
    psoup = BeautifulSoup(page, 'lxml')

    namefind = psoup.find('h1', {'class': 'title'})
    name = namefind.text

    valfind = psoup.find('div', {'class': 'price last'})
    valtext = valfind.text[:-1].strip().replace(',', '')
    value = float(valtext)

    return (name, value)

def scrape_and_store(link: str, db: database) -> Tuple[str, float]:
    name, price = scrape(link)
    db.add_datapt(name, datetime.now(), price)
    return (name, price)

def autoscrape(link: str, minutes_per_scrape: float, db: database):
    while True:
        name, price = scrape_and_store(link, db)
        print("scraped data:", name + ",", price,  "₽")
        time.sleep(minutes_per_scrape * 60)

def graph(name: str, db: database):
    data = db.get_item_data(name)
    print(data)
    plt.plot(data.keys(), data.values(), )
    plt.show()