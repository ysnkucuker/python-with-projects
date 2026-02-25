import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

target_url = "https://www.yasinkucuker.com"
foundLinks = []

def make_req(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def crawl(url):
    soup = make_req(url)

    for link in soup.find_all("a"):
        href = link.get("href")

        if href:
            full_url = urljoin(target_url, href)  # önemli kısım

            # fragment (#) temizle
            full_url = full_url.split("#")[0]

            if target_url in full_url and full_url not in foundLinks:
                foundLinks.append(full_url)
                print(full_url)
                crawl(full_url)

crawl(target_url)