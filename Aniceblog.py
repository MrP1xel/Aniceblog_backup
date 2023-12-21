import requests
from bs4 import BeautifulSoup

LIST_URL = []
ANICE_URL_ARTICLES = []
MEDIAPART_URL = "https://blogs.mediapart.fr"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
for x in range(1,14):
        LIST_URL.append("https://blogs.mediapart.fr/anice-lajnef/blog?page=" + str(x))


def get_url(url):
        URLS = []
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        post_list = soup.find("ul", {"class": "post-list"})
        article_links = [link.get("href") for link in post_list.find_all("a")]
        for article in article_links:
                if "mediapart" not in article:
                        URLS.append((MEDIAPART_URL).rstrip() + article.lstrip())
        return URLS

for url in LIST_URL:
        for article in get_url(url):
                ANICE_URL_ARTICLES.append(article.rstrip())


def download_page(url):
        response = requests.get(url)
        html = response.text
        filename = url.split('/')[-1] + str(".html")
        print(filename)
        with open(filename, "w", encoding="utf-8") as f:
                 f.write(html)

for url in ANICE_URL_ARTICLES:
        download_page(url)
        print("downloading: " , url)
