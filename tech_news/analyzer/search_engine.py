from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    links = []
    query = {"title": {"$regex": title, "$options": 'i'}}

    for item in search_news(query):
        links.append((item["title"], item["url"]))
    return links


# Requisito 8
def search_by_date(date):
    links = []
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        for item in search_news({"timestamp": date}):
            links.append((item["title"], item["url"]))
    except ValueError:
        raise ValueError("Data inválida")
    return links


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    links = []

    for item in search_news(query):
        links.append((item["title"], item["url"]))

    return links
