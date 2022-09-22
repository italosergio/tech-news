from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = sorted(find_news(), key=lambda x: x["comments_count"], reverse=1)
    sorted(news, key=lambda x: x["title"])

    max_iterations = 5
    news_list_size = len(news)

    if news_list_size < max_iterations:
        max_iterations = news_list_size

    top_5 = list()
    for index in range(0, max_iterations):
        top_5.append((news[index]["title"], news[index]["url"]))

    return top_5


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
