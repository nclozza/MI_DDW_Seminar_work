# Returns the quantity of citations founded
def get_total_citations_in_HTML(page):
    return len(page.citations)


# Adds to the CitationType object the type of the citation founded in the dump
def add_dump_citation_per_type(citation_type, dump_citation):
    citetype = dump_citation['citetype']
    setattr(citation_type, citetype, getattr(citation_type, citetype) + 1)
