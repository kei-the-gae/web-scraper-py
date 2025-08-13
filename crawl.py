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
            except Exception as err:
                print(f"{str(err)}: {href}")

    return urls


def crawl_page(base_url, current_url=None, pages=None):
    if current_url is None:
        current_url = base_url
    if pages is None:
        pages = {}

    base_url_obj = urlparse(base_url)
    current_url_obj = urlparse(current_url)
    if current_url_obj.netloc != base_url_obj.netloc:
        return pages

    normalized_url = normalize_url(current_url)

    if normalized_url in pages:
        pages[normalized_url] += 1
        return pages

    pages[normalized_url] = 1

    print(f"crawling {current_url}")
    html = safe_get_html(current_url)
    if html is None:
        return pages

    next_urls = get_urls_from_html(html, base_url)
    for next_url in next_urls:
        pages = crawl_page(base_url, next_url, pages)

    return pages


def get_html(url):
    try:
        res = requests.get(url)
    except Exception as err:
        raise Exception(f"network error while fetching {url}: {err}")

    if res.status_code > 399:
        raise Exception(f"got HTTP error: {res.status_code} {res.reason}")

    content_type = res.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise Exception(f"got non-HTML response: {content_type}")

    return res.text


def safe_get_html(url):
    try:
        return get_html(url)
    except Exception as err:
        print(f"{err}")
        return None
