from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests


def normalize_url(url):
    parsed_url = urlparse(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()


def get_urls_from_html(html, base_url):
    urls = []
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.find_all("a")

    for anchor in anchors:
        if href := anchor.get("href"):
            try:
                absolute_url = urljoin(base_url, href)
                urls.append(absolute_url)
            except Exception as e:
                print(f"{str(e)}: {href}")

    return urls


def get_html(url):
    try:
        res = requests.get(url)
    except Exception as e:
        raise Exception(f"network error while fetching {url}: {e}")

    if res.status_code > 399:
        raise Exception(f"got HTTP error: {res.status_code} {res.reason}")

    content_type = res.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise Exception(f"got non-HTML response: {content_type}")

    return res.text
