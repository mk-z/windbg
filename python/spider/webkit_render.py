#!/usr/bin/python
# -*- coding: utf-8 -*-

try: 
    from PySide.QtGui import QApplication
    from PySide.QtCore import *
    from PySide.QtWebKit import QWebView
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *
import lxml.html
import download


def direct_download(url):
    downloader = download.Downloader()
    return downloader(url)

def webkit_download(url):
    app = QApplication([])
    webview = QWebView()
    webview.loadFinished.connect(app.quit)
    webview.load(url)
    app.exec_() # delay here until download finished
    return webview.page().mainFrame().toHtml()


def parse(html):
    tree = lxml.html.fromstring(html)
    print tree.cssselect('#result')[0].text_content()


def main(): 
    url = 'http://example.webscraping.com/dynamic'
    parse(direct_download(url))
    parse(webkit_download(url))
    return

    print len(r.html)


if __name__ == '__main__':
    main()