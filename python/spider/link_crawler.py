
#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urlparse
import download

def get_links(html):
    """Return a list of links from html
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return webpage_regex.findall(html)


def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download.download(url)
        for link in get_links(html):
            if re.match(link_regex, link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

if __name__ == "__main__":
    link_crawler("http://example.webscraping.com", '/(index|view)')