import datetime

import requests
from bs4 import BeautifulSoup

import src.HTMLCrawler.citation as citation
import src.HTMLCrawler.configuration as configuration
import src.HTMLCrawler.content as content
import src.HTMLCrawler.reference as reference
import src.common.url_type as url_type
import src.common.util as util
from src.common.object import Object
from src.model.HTMLPage import HTMLPage


def main(urls, craw_delay, headers):
    pages = Object()
    for url in urls:
        # DEBUG
        print('Crawling: ' + url)

        source = requests.get(url, headers).text
        initial_time = datetime.datetime.now()
        soup = BeautifulSoup(source, "html5lib")
        name = util.get_name_from_url(url)
        setattr(pages, name, HTMLPage())

        references = reference.find_all(soup)
        getattr(pages, name).citations = citation.find_all(soup, references)
        getattr(pages, name).content = content.extract_text(soup, name)

        util.wait_crawl_delay(initial_time, craw_delay)


url_array = util.get_urls(url_type.DEBUG)
main(url_array, configuration.CRAWL_DELAY, configuration.HEADERS)
