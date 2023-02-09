import requests
import time
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout
from parsel import Selector
from tech_news.database import create_news


fake_headers = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url: str):
    time.sleep(1)
    try:
        res = requests.get(url, headers=fake_headers, timeout=3)
        res.raise_for_status()
    except (ConnectTimeout, HTTPError, ReadTimeout):
        return None

    return res.text


# Requisito 2
def scrape_updates(html_content):
    selec = Selector(html_content)
    return selec.css("h2 > a ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selec = Selector(html_content)
    return selec.css("div.nav-links > a.next ::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    selec = Selector(html_content)

    url = selec.css("link[rel='canonical'] ::attr(href)").get()
    title = selec.css("h1.entry-title ::text").get().strip()
    timestamp = selec.css("ul > li.meta-date ::text").get()
    writer = selec.css("span.author > a ::text").get()
    reading_time = selec.css("li.meta-reading-time ::text").re_first(r"\d+")
    summary = "".join(
        selec.css("div.entry-content > p:first-of-type ::text")
        .getall()).strip()
    category = selec.css("span.label ::text").get()

    obj = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }
    return obj


# Requisito 5
def get_tech_news(amount):
    html = fetch("https://blog.betrybe.com")
    url_list = scrape_updates(html)
    items = []

    while len(url_list) < amount:
        next_page = scrape_next_page_link(html)
        html = fetch(next_page)
        url_list += scrape_updates(html)

    for url in url_list[:amount]:
        res = fetch(url)
        data = scrape_news(res)
        items.append(data)

    create_news(items)
    return items
