""" Question-9:
Given a URL, download that and parse 
and download all links inside that page 
    in asyncio 
    BeautifulSoup for parsing html, requests for downloading"""

import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import sys

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def fetch(ses, url):
    try:
        async with ses.get(url, timeout=10) as response:
            response.raise_for_status()
            text = await response.text()
            print(f"Downloaded: {url}")
            return url, text
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url, ""


async def get_links(ses, base_url):
    _, html = await fetch(ses, base_url)
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for tag in soup.find_all("a", href=True):
        full_url = urljoin(base_url, tag['href'])
        if full_url.startswith("http"):
            links.add(full_url)
    return links


async def download_links(ses, links):
    tasks = [fetch(ses, url) for url in links]
    return await asyncio.gather(*tasks)


async def main(start_url):
    async with aiohttp.ClientSession() as ses:
        links = await get_links(ses, start_url)
        print(f"Found {len(links)} links")
        pages = await download_links(ses, links)
        os.makedirs("downloaded_pages", exist_ok=True)
        for i, (url, content) in enumerate(pages, start=1):
            if content:
                with open(f"downloaded_pages/page_{i}.html", "w", encoding="utf-8") as f:
                    f.write(content)

        print(f"Downloaded {len(pages)} pages.")


if __name__ == '__main__':
    import time
    start_url = "https://www.bing.com/search?q=covasant&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=covasan&sc=12-7&sk=&cvid=184D9A2CD026433A93FC239B3CB9321F"  # Replace with the target URL
    st = time.time()
    asyncio.run(main(start_url))
    print("Time taken:", time.time() - st, "secs")
