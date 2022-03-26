import os
import string
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nature.com"


def get_articles_from_response(response, requested_type, directory):
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("article")
    if articles:
        for article in articles:
            article_type = article.find("span", {"class": "c-meta__type"}).text
            if article_type == requested_type:
                title = article.find("a").text.strip().replace(string.punctuation, "").replace("’", "").replace("?",
                                                                                                                "").replace(
                    " ", "_")
                link = article.find("a", href=True)["href"]
                article_url = f"{BASE_URL}{link}"
                filename = directory / f"{title}.txt"

                response = requests.get(article_url)
                soup2 = BeautifulSoup(response.content, "html.parser")
                content = soup2.find("div", {"class": "c-article-body"}).text.strip()
                content_binary = bytes(content, "utf-8")

                with open(filename, 'wb') as source:
                    source.write(content_binary)


def browse_pages(pages, articles_type):
    for number in range(1, pages + 1):
        page_dir = Path.cwd() / f"Page_{number}"
        os.mkdir(page_dir)
        pages_url = f"{BASE_URL}/nature/articles?sort=PubDate&year=2020"
        url = f"{pages_url}&page={number}"
        response = requests.get(url)
        get_articles_from_response(response, articles_type, page_dir)

    print("Saved all articles.")


if __name__ == "__main__":
    pages = int(input())
    articles_type = input()
    browse_pages(pages, articles_type)
