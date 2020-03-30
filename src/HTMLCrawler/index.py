import datetime

import requests
from bs4 import BeautifulSoup

import src.HTMLCrawler.citation as citation
import src.HTMLCrawler.configuration as configuration
import src.HTMLCrawler.reference as reference
import src.common.util as util
from src.common.object import Object
from src.model.HTMLPage import HTMLPage


def main(urls, craw_delay, headers):
    pages = Object()
    for url in urls:
        source = requests.get(url, headers).text
        initial_time = datetime.datetime.now()
        soup = BeautifulSoup(source, "html5lib")
        name = util.get_name_from_url(url)
        setattr(pages, name, HTMLPage())

        references = reference.find_all(url, soup)
        getattr(pages, name).citations = citation.find_all(url, soup, references)

        util.wait_crawl_delay(initial_time, craw_delay)


main(configuration.URLS, configuration.CRAWL_DELAY, configuration.HEADERS)
