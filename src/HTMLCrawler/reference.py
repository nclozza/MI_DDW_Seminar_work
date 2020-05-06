# Crawls and returns all the references founded
def find_all(soup):
    try:
        references = soup.find_all("ol", {"class": "references"})
        reference_array = []

        for elem in references:
            reference = elem.find_all("li")

            for ref in reference:
                reference_array.append(ref)

        return reference_array
    except Exception as e:
        print(e)


# Returns the text of a specific reference
def get_text(reference):
    try:
        span = reference.find("span", {"class": "reference-text"})
        text = ""
        if span is not None:
            for node in span.contents:
                if isinstance(node, str):
                    text += node
                elif node.name != "style":
                    text += node.text
                    if node.name != "a":
                        href_array = node.find_all("a", href=True)
                        for href in href_array:
                            text += " \"" + href['href'] + "\""
                    else:
                        text += " \"" + node['href'] + "\""
        return text
    except Exception as e:
        print(e)
