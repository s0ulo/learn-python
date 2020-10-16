from datetime import datetime

import requests
from bs4 import BeautifulSoup
from webapp.db import db
from webapp.news.models import News


def get_html(url):  # scrape html code from url
    try:
        result = requests.get(url)  # loal html into result
        result.raise_for_status()
        return result.text  # convert html to text for further analysis
    except (requests.RexuestException, ValueError):
        return False


def get_python_news():
    html = get_html("https://www.python.org/blogs/")  # get text html from url
    if html:
        # create parsed (searchable) object version?
        soup = BeautifulSoup(html, "html.parser")

        # find all embedded <li> in -> exact <ul> named 'list-recent-posts'
        news_list = soup.find("ul", class_="list-recent-posts").findAll("li")

        # result_news = []  # list of dicts with news from every <li>
        for news in news_list:
            title = news.find("a").text  # get news title from <a>
            url = news.find("a")["href"]  # note the ['href'] cuz it's dict obj
            published = news.find("time").text  # get time from <time>
            try:
                published = datetime.strptime(published, "%Y-%m-%d")
            except (ValueError):
                published = datetime.now()
            save_news(title, url, published)


def save_news(title, url, published):  # export news object to database

    # Integrity test (search for dubs)
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)  # show how many dubs found

    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)  # add object to database session in Alchemy
        db.session.commit()  # commit (record) object to database
