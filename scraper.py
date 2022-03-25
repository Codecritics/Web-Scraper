import string

from bs4 import BeautifulSoup
from requests import get

if __name__ == '__main__':
    URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    r = get(URL)
    saved_articles = list()
    soup = BeautifulSoup(r.content, 'html.parser')

    article_list = soup.find("ul", class_="app-article-list-row")
    articles_types = [type_.text.strip('\n') for type_ in
                      article_list.find_all_next("span", {"data-test": "article.type"})]

    news_indexes = [i for i in range(len(articles_types)) if articles_types[i] == "News"]

    punctuation_trans = str.maketrans('', '', string.punctuation.replace('_', ''))
    articles_titles = article_list.find_all_next("a", class_="c-card__link u-link-inherit")

    articles_links = article_list.find_all_next('a', {"data-track-action": "view article"})
    for news_index in news_indexes:
        article_link = "https://www.nature.com" + articles_links[news_index].get('href')
        article_content = get(article_link).content
        soup_article = BeautifulSoup(article_content, 'html.parser')

        content_to_write = soup_article.find("div", class_="c-article-body u-clearfix").text.encode("UTF-8")

        article_filename = articles_titles[news_index].text.rstrip().lstrip().replace(' ', '_').translate(
            punctuation_trans) + ".txt"

        with open(article_filename,
                  'wb') as file:
            file.write(content_to_write)
        saved_articles.append(article_filename)
        
    print("Saved articles:  ")
    print(saved_articles)
