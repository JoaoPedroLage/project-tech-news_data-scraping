import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:

            return response.text
        else:

            return None
    except requests.Timeout:

        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    news_url = selector.css(".cs-overlay-link::attr(href)").getall()

    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page_link = selector.css("a.next ::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("[rel='canonical']::attr(href)").get().strip()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url::text").get()
    comments_count = len(
        selector.css(".comment-list li").getall())
    summary = selector.css(
        '.entry-content > p:first-of-type *::text').getall()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".label::text").get()

    return {
            'url': url, 'title': title,
            'timestamp': timestamp, 'writer': writer,
            'category': category, 'summary': ''.join(summary).strip(),
            'comments_count': comments_count, 'tags': tags
            }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
