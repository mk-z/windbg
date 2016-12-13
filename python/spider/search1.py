#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import string
import download
import mongo_cache

def main():
    template_url = 'http://example.webscraping.com/ajax/search.json?page={}&page_size=10&search_term={}'
    countries = set()
    downloader = download.Downloader(mongo_cache.MongoCache())

    for letter in string.lowercase:
        page = 0
        while True:
            html = downloader(template_url.format(page, letter))
            print html
            try:
                ajax = json.loads(html)
            except ValueError as e:
                print e
                ajax = None
            else:
                for record in ajax['records']:
                    countries.add(record['country'])
            page += 1
            if ajax is None or page >= ajax['num_pages']:
                break
    
    open('countries.txt', 'w').write('\n'.join(sorted(countries)))


if __name__ == '__main__':
    main()