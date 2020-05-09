import sys

import reference as reference

sys.path.append('../')
from model.HTMLCitation import HTMLCitation


# Crawls and returns all the references founded
def find_all(soup, references):
    try:
        citations = soup.find_all("sup", {"class": "reference"})
        citation_array = []

        for citation in citations:
            obj = HTMLCitation()
            obj.citation = citation
            obj.reference = find_reference_by_citation(citation, references)
            if obj.reference is not None:
                obj.text = reference.get_text(obj.reference)
                citation_array.append(obj)

        return citation_array
    except Exception as e:
        print(e)


# Finds and returns a reference of a specific citation
def find_reference_by_citation(citation, references):
    try:
        for ref in references:
            reference_id = ref.get('id')
            href = get_href(citation)
            if reference_id == href:
                return ref

        return None
    except Exception as e:
        print(e)


# Returns the href of a citation
def get_href(citation):
    try:
        href = citation.find("a", href=True)
        if href is not None:
            return href['href'][1:]
        else:
            return None
    except Exception as e:
        print(e)
