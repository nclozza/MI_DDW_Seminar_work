def get_all(url, soup):
    try:
        # DEBUG
        print('Crawled references from: ' + url)

        references = soup.find_all("ol", {"class": "references"})
        reference_array = []

        for elem in references:
            reference = elem.find_all("li")

            for ref in reference:
                reference_array.append(ref)

        return reference_array
    except Exception as e:
        print(e)


def get_all_span_text(references):
    try:
        span_array = []
        for reference in references:
            span = reference.find("span", {"class": "reference-text"})
            span_array.append(span)

        return span_array
    except Exception as e:
        print(e)


def print_all(references):
    print("CANTIDAD DE REFERENCIAS: " + str(len(references)))
    for reference in references:
        print(reference)
