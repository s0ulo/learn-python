import requests
from webapp.db import db
from webapp.news.models import News


def get_html(url):  # scrape html code from url
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0"
    }
    try:
        result = requests.get(url, headers=headers)  # loal html into result
        result.raise_for_status()
        return result.text  # convert html to text for further analysis
    except (requests.RexuestException, ValueError):
        return False


def save_news(title, url, published):  # export news object to database

    # Integrity test (search for dubs)
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)  # show how many dubs found

    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)  # add object to database session in Alchemy
        db.session.commit()  # commit (record) object to database
