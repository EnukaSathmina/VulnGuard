import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def crawl_website(url: str):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(response.text, "html.parser")

    links = set()

    for tag in soup.find_all("a", href=True):
        full_url = urljoin(url, tag["href"])

        if urlparse(full_url).netloc == urlparse(url).netloc:
            links.add(full_url)

    return {
        "input_url": url,
        "total_links": len(links),
        "links": list(links)
    }