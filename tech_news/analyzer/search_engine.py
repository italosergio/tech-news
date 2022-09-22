from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_by_title = search_news({"title": {"$regex": title, "$options": "i"}})
    news_by_title_semantic = [
        (news["title"], news["url"]) for news in news_by_title
    ]

    return news_by_title_semantic


# Requisito 7
def search_by_date(date):
    news = list()
    try:
        date_parsed = datetime.strptime(date, "%Y-%m-%d")
        date_string = datetime.strftime(date_parsed, "%d/%m/%Y")
        news_by_date = search_news({"timestamp": date_string})
        news = [(new["title"], new["url"]) for new in news_by_date]
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_by_tag = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news_by_tag_semantic = [(new["title"], new["url"]) for new in news_by_tag]

    return news_by_tag_semantic


# Requisito 9
def search_by_category(category):
    news_by_category = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    news_by_category_semantic = [
        (new["title"], new["url"]) for new in news_by_category
    ]

    return news_by_category_semantic
