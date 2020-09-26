import requests
from bs4 import BeautifulSoup


def get_python_news():
    html = get_html('https://www.python.org/blogs/')  # get text html from url
    if html:
        # create parsed object version?
        soup = BeautifulSoup(html, 'html.parser')

        # find all embedded <li> in -> exact <ul> named 'list-recent-posts'
        news_list = soup.find('ul', class_='list-recent-posts').findAll('li')

        result_news = []  # list of dicts with news from every <li>
        for news in news_list:
            title = news.find('a').text  # get news title from <a>
            url = news.find('a')['href']  # note the ['href'] cuz it's dict obj
            published = news.find('time').text  # get time from <time>
            result_news.append({
                'title': title,
                'url': url,
                'published': published
            })
        return result_news
    return False


def get_html(url):
    try:
        result = requests.get(url)  # loal html entirely from url
        result.raise_for_status()
        return result.text  # text represent html
    except(requests.RexuestException, ValueError):
        return False
