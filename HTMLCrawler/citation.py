import requests
from bs4 import BeautifulSoup


def get_all(urls, citations, headers):
    for url in urls:
        name = url[url.rfind('/') + 1:]
        setattr(citations, name, get(url, headers))

        # DEBUG
        print("EN LA PAGINA DE: " + name)
        print_all(getattr(citations, name))


def get(url, headers):
    try:
        print('Crawled citations from: ' + url)
        source = requests.get(url, headers).text
        soup = BeautifulSoup(source, "html5lib")

        citations = soup.find_all("sup", {"class": "reference"})
        citation_array = []

        for citation in citations:
            citation_array.append(citation)

        return citation_array
    except Exception as e:
        print(e)


def print_all(citations):
    for citation in citations:
        print(citation)
