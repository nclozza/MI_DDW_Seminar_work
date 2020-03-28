def get_all(url, soup):
    try:
        # DEBUG
        print('Crawled citations from: ' + url)

        citations = soup.find_all("sup", {"class": "reference"})
        citation_array = []

        for citation in citations:
            citation_array.append(citation)

        return citation_array
    except Exception as e:
        print(e)


def get_all_href(citations):
    try:
        href_array = []
        for citation in citations:
            href = citation.find("a", href=True)
            value = href['href'][1:]
            href_array.append(value)

        return href_array
    except Exception as e:
        print(e)


def print_all(citations):
    print("CANTIDAD DE CITACIONES: " + str(len(citations)))
    for citation in citations:
        print(citation)
