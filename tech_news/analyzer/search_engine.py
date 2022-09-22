from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({'title': {'$regex': title, '$options': 'i'}})
    news_by_title_semantic = [(news['title'], news['url']) for news in news_by_title]

    return news_by_title_semantic


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
