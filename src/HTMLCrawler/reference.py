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


def get_all_text(references):
    try:
        text_array = []
        for reference in references:
            span = reference.find("span", {"class": "reference-text"})
            text = extract_text_from_span(span)
            text_array.append(text)
        return text_array
    except Exception as e:
        print(e)


def extract_text_from_span(span):
    text = ""
    for node in span.contents:
        if isinstance(node, str):
            text += node + " | "
        elif node.name != "style":
            if node.text != "":
                text += node.text + " | "
            if node.name != "a":
                href_array = node.find_all("a", href=True)
                for href in href_array:
                    text += href['href'] + " | "
            else:
                text += node['href'] + " | "
    return text


def print_all(references):
    print("CANTIDAD DE REFERENCIAS: " + str(len(references)))
    for reference in references:
        print(reference)
