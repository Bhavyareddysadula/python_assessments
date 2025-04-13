"""Question-8:
Given a URL, download that and parse 
and download all links inside that page 
    Use ThreadPoolExecutor or ProcessPoolExecutor 
    BeautifulSoup for parsing html, requests for downloading"""

# Using threads

from bs4 import BeautifulSoup
from urllib.parse import urljoin 
import time
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def download(url):
    try:
        print(f"Downloading: {url}")
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return url, res.text
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return url, ""

def get_links(base_url):
    _, html = download(base_url)
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a in soup.find_all('a', href=True):
        full_url = urljoin(base_url, a['href'])
        if full_url.startswith("http"):
            links.add(full_url)
    return links

def download_links(links):
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(download, link) for link in links]
        for future in as_completed(futures):
            url, content = future.result()
            results.append((url, content))
    return results

if __name__ == '__main__':
    start_url = "https://www.bing.com/search?q=covasant&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=covasan&sc=12-7&sk=&cvid=184D9A2CD026433A93FC239B3CB9321F"  # Replace with your desired URL
    print(f"Fetching and parsing: {start_url}")

    st = time.time()
    links = get_links(start_url)
    print(f"Found {len(links)} links")

    downloaded_pages = download_links(links)

    print(f"Downloaded {len(downloaded_pages)} pages.")
    print("Time taken:", time.time() - st, "secs")


