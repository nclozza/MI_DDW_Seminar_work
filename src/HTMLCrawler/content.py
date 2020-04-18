import json

import src.DumpCrawler.configuration as configuration


def extract_text(soup, name):
    try:
        text_content = soup.find("div", {"id": "mw-content-text"})
        content = text_content.find_all(["p", "h2", "h3", "h4"])

        text = name + "\n"
        for index, elem in enumerate(content):
            if elem.name == "p":
                text += elem.text
            elif len(content) != index + 1:
                next_elem = content[(index + 1)]
                if next_elem.name == "p":
                    title = elem.find("span", {"class": "mw-headline"})
                    text += "\n" + title.text + "\n"

        return text
    except Exception as e:
        print(e)


def replace_citations_in_content(page, name):
    try:
        path = configuration.JSONL_FOLDER_PATH + name + configuration.JSONL_EXTENSION

        with open(path) as infile:
            for line in infile:
                dump_citation = json.loads(line)
                max_count = 0
                actual_count = 0
                html_citation = None

                for citation in page.citations:

                    for attr, value in dump_citation.items():
                        if is_text_in_citation(citation, value):
                            actual_count += 1

                    if actual_count > max_count:
                        html_citation = citation
                        max_count = actual_count

                    actual_count = 0

                if html_citation:
                    page.content = get_html_content_with_dump_citation(page.content, dump_citation,
                                                                       html_citation.citation.text)
    except Exception as e:
        print(e)


def is_text_in_citation(citation, text):
    return text in citation.text


def get_html_content_with_dump_citation(html_content, dump_citation, citation):
    text = json.dumps(dump_citation)
    return html_content.replace(citation, text)


def save_json(type, name, url, content):
    result = {
        "url": url,
        "content": content
    }
    path = "../data/result/" + type.lower() + "/" + name + ".json"
    with open(path, 'w') as outfile:
        json.dump(result, outfile)
