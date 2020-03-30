import datetime

import citation
import requests
from bs4 import BeautifulSoup

import src.HTMLCrawler.configuration as configuration
import src.HTMLCrawler.reference as reference
import src.common.util as util
from src.common.object import Object
from src.model.HTMLPage import HTMLPage


def main(urls, craw_delay, headers):
    pages = Object()
    for url in urls:
        initial_time = datetime.datetime.now()
        source = requests.get(url, headers).text
        soup = BeautifulSoup(source, "html5lib")
        name = util.get_name_from_url(url)
        setattr(pages, name, HTMLPage())

        getattr(pages, name).citation.citations = citation.get_all(url, soup)
        getattr(pages, name).citation.href = citation.get_all_href(getattr(pages, name).citation.citations)

        getattr(pages, name).reference.references = reference.get_all(url, soup)
        getattr(pages, name).reference.text = reference.get_all_text(getattr(pages, name).reference.references)

        util.wait_crawl_delay(initial_time, craw_delay)


main(configuration.URLS, configuration.CRAWL_DELAY, configuration.HEADERS)

# DEBUG
# print("Buenos Aires")
# print("CANTIDAD DE CITACIONES: " + str(len(pages.Buenos_Aires.citation.citations)))
# print("CANTIDAD DE REFERENCIAS: " + str(len(pages.Buenos_Aires.reference.references)))
# print("Paris")
# print("CANTIDAD DE CITACIONES: " + str(len(pages.Paris.citation.citations)))
# print("CANTIDAD DE REFERENCIAS: " + str(len(pages.Paris.reference.references)))
# print("Prague")
# print("CANTIDAD DE CITACIONES: " + str(len(pages.Prague.citation.citations)))
# print("CANTIDAD DE REFERENCIAS: " + str(len(pages.Prague.reference.references)))
