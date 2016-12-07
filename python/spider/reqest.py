#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import re
from bs4 import BeautifulSoup
import lxml.html
from download import download

FIELDS = ('area', 'population', 'iso', 'country', 'capital',
    'continent', 'tld', 'currency_code', 'currency_name', 'phone', 
    'postal_code_format', 'postal_code_regex', 'languages', 
    'neighbours')

def re_scraper(html):
    results = {}
    for field in FIELDS:
        results[field] = re.search('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>' % field, html).groups()[0]
    return results

def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_%s__row' % field).find('td', class_='w2p_fw').text
    return results

def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in FIELDS:        
        results[field] = tree.cssselect('table> tr#places_%s__row> td.w2p_fw' % field)[0].text_content()
        #print "lxml:%s   result: %s" % (field, results[field])
    return results



if __name__ == "__main__":
    NUM_ITERATIONS = 1000
    html = download('http://example.webscraping.com/places/view/United-Kingdom-239')
    for name, scraper in [('Regular expressions', re_scraper),
        ('BeautifulSoup', bs_scraper),
        ('Lxml', lxml_scraper)]:
        start = time.time()
        for i in range(NUM_ITERATIONS):
            if scraper == re_scraper:
                re.purge()
            result = scraper(html)
            assert(result['phone']=='44')
        end = time.time()
        print '%s: %.2f seconds' % (name, end-start)