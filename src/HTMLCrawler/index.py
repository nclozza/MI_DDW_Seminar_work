import datetime
import time

import citation
import configuration
import reference
import requests
from bs4 import BeautifulSoup

import src.common.util as util
from src.common.object import Object

citations = Object()
references = Object()

for url in configuration.URLS:
    initial_time = datetime.datetime.now()

    source = requests.get(url, configuration.HEADERS).text
    soup = BeautifulSoup(source, "html5lib")

    name = util.get_name_from_url(url)

    setattr(citations, name, citation.get_all(url, soup))
    # DEBUG
    print("EN LA PAGINA DE: " + name)
    citation.print_all(getattr(citations, name))

    setattr(references, name, reference.get_all(url, soup))
    # DEBUG
    print("EN LA PAGINA DE: " + name)
    reference.print_all(getattr(references, name))

    final_time = datetime.datetime.now()
    time_diff = util.get_mili_time_diff(initial_time, final_time)

    if time_diff < configuration.CRAWL_DELAY:
        time.sleep((configuration.CRAWL_DELAY - time_diff) / 1000)

# DEBUG
print("Buenos Aires")
print("CANTIDAD DE CITACIONES: " + str(len(citations.Buenos_Aires)))
print("CANTIDAD DE REFERENCIAS: " + str(len(references.Buenos_Aires)))
print("Paris")
print("CANTIDAD DE CITACIONES: " + str(len(citations.Paris)))
print("CANTIDAD DE REFERENCIAS: " + str(len(references.Paris)))
print("Prague")
print("CANTIDAD DE CITACIONES: " + str(len(citations.Prague)))
print("CANTIDAD DE REFERENCIAS: " + str(len(references.Prague)))
