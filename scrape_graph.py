from database import database
from bs4 import BeautifulSoup
import requests
from typing import Tuple
from datetime import datetime
import time
import matplotlib.pyplot as plt


def scrape(link: str) -> Tuple[str, float, str]:
    page = requests.get(link).text
    psoup = BeautifulSoup(page, 'lxml')

    namefind = psoup.find('h1', {'class': 'title'})
    name = namefind.text

    valfind = psoup.find('div', {'class': 'price last'})
    valtext = valfind.text[:-1].replace(',', '').replace(' ', '')
    value = float(valtext)

    updfind = psoup.find('div', {'class': 'updated-block'})
    updtext = updfind.text

    return (name, value, updtext)

def scrape_and_store(link: str, db: database) -> Tuple[str, float, datetime]:
    name, price, updated = scrape(link)
    t = datetime.now()
    db.add_datapt(name, t, price)
    return (name, price, t, updated)

def autoscrape(link: str, minutes_per_scrape: float, db: database):
    while True:
        name, price, t, updated = scrape_and_store(link, db)
        print(t.strftime("%H:%M:%S") + " - scraped data:", name + ",", price,  "₽", updated)
        time.sleep(minutes_per_scrape * 60)

def graph(name: str, db: database):
    data = db.get_item_data(name)
    plt.plot(data.keys(), data.values(), 'go-')
    plt.show()
