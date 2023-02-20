import requests
import os
from dotenv import load_dotenv

load_dotenv()
# https://newsapi.org/ get apikey
API_KEY = os.getenv("API_KEY")

URL = "https://newsapi.org/v2/top-headlines?"

CATEGORIES = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology",
]


def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "br",
        "apiKey": API_KEY,
    }
    return get_articles(query_parameters)


def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "br",
        "apiKey": API_KEY,
    }
    return get_articles(query_parameters)


def get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()["articles"]

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result["title"])
        print(result["url"])
        print("")


if __name__ == "__main__":
    get_articles_by_category(CATEGORIES[3])
