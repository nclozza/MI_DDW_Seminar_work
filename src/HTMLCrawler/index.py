import datetime

import requests
from bs4 import BeautifulSoup

import src.HTMLCrawler.citation as citation
import src.HTMLCrawler.configuration as configuration
import src.HTMLCrawler.content as content
import src.HTMLCrawler.reference as reference
import src.common.configuration as url_configuration
import src.common.util as util
from src.common.object import Object
from src.model.HTMLPage import HTMLPage


def main(craw_delay, headers):
    pages = Object()

    for type in url_configuration.URL_TYPE:
        urls = util.get_available_urls(type)

        for url in urls:
            # DEBUG
            print('Crawling: ' + url)

            source = requests.get(url, headers).text
            initial_time = datetime.datetime.now()
            soup = BeautifulSoup(source, "html.parser")
            name = util.get_name_from_url(url)
            setattr(pages, name, HTMLPage())

            references = reference.find_all(soup)
            getattr(pages, name).citations = citation.find_all(soup, references)
            getattr(pages, name).content = content.extract_text(soup, name)
            content.replace_citations_in_content(getattr(pages, name), name)
            content.save_json(type, name, url, getattr(pages, name).content)

            util.wait_crawl_delay(initial_time, craw_delay)


main(configuration.CRAWL_DELAY, configuration.HEADERS)
