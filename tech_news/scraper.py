import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"User-Agent": "Fake user-agent"}
        )
        response.raise_for_status()
        time.sleep(1)
        return response.text

    except requests.ReadTimeout:
        return None

    except requests.exceptions.HTTPError:
        return None


# Requisito 2
def scrape_novidades(html_content):
    page_news_links = (
        Selector(html_content).css("a.cs-overlay-link::attr(href)").getall()
    )

    if not page_news_links:
        return []

    return page_news_links


# Requisito 3
def scrape_next_page_link(html_content):
    next_page_link = (
        Selector(html_content)
        .css("a.next.page-numbers::attr(href)")
        .get()
    )
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
