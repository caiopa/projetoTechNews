import requests
import time
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout

# Requisito 1
def fetch(url: str):
    time.sleep(1)
    try:
        res = requests.get(url, headers={ "user-agent": "Fake user-agent" }, timeout=3)
        res.raise_for_status()
    except (ConnectTimeout, HTTPError, ReadTimeout):
        return None

    return res.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
