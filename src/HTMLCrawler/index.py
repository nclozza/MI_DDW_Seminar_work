import datetime
import sys

import citation as citation
import configuration as configuration
import content as content
import reference as reference
import requests
from bs4 import BeautifulSoup

sys.path.append('../')
import common.configuration as url_configuration
import common.util as util
from common.object import Object
from model.HTMLPage import HTMLPage


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
