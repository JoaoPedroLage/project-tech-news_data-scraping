from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    search = []
    news = search_news({"title": {"$regex": f"{title.lower()}"}})

    for new in news:
        search.append(tuple([new['title'], new['url']]))

    return search


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        search = []
        if not bool(datetime.strptime(date, "%Y-%m-%d")):
            raise ValueError

        input = datetime.fromisoformat(date)
        date_search = datetime.strftime(input, "%d/%m/%Y")
        news = search_news({"timestamp": date_search})

        for new in news:
            search.append(tuple([new['title'], new['url']]))

        return search

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""