from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = sorted(find_news(), key=lambda x: x["comments_count"], reverse=1)
    sorted(news, key=lambda x: x["title"])

    max_iterations = 5
    news_list_size = len(news)

    if news_list_size < max_iterations:
        max_iterations = news_list_size

    top_5 = [(new["title"], new["url"]) for new in news[:max_iterations]]

    return top_5


# Requisito 11
def top_5_categories():
    categories = [new["category"] for new in find_news()]

    category_count = [(name, categories.count(name)) for name in categories]
    categories_sorted = sorted(category_count, key=lambda x: (-x[1], x[0]))

    categories = [category[0] for category in categories_sorted]

    categories_list = []
    for category in categories:
        if category not in categories_list:
            categories_list.append(category)

    return categories_list
