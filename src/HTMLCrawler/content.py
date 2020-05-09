import json
import sys

import statistic as statistic

sys.path.append('../')
import DumpCrawler.configuration as configuration
from model.HTMLResult import HTMLResult


# Crawls and returns all the content text of the page
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


# Loops all the dumps citations and try to found a match between the html citation and the dump citation
# If the citation is matched, it is replaced in the content of the page
# Collects data to add in the statistics
def replace_citations_in_content(page, name):
    try:
        path = configuration.JSONL_FOLDER_PATH + name + configuration.JSONL_EXTENSION

        with open(path) as infile:
            for line in infile:
                dump_citation = json.loads(line)
                max_count = 0
                actual_count = 0
                html_citation = None
                page.statistic.total_citations_in_dump += 1
                statistic.add_dump_citation_per_type(page.statistic.total_citations_in_dump_per_type, dump_citation)

                for citation in page.citations:
                    for attr, value in dump_citation.items():
                        if is_text_in_citation(citation, value):
                            actual_count += 1

                    if actual_count > max_count:
                        html_citation = citation
                        max_count = actual_count

                    actual_count = 0

                if html_citation:
                    page.statistic.citations_matched += 1
                    statistic.add_dump_citation_per_type(page.statistic.citations_matched_per_type, dump_citation)
                    page.content = get_html_content_with_dump_citation(page.content, dump_citation,
                                                                       html_citation.citation.text)
    except Exception as e:
        print(e)


# Checks if a text is found in the citation
def is_text_in_citation(citation, text):
    return text in citation.text


# Replaces the citation matched in the content of the page
def get_html_content_with_dump_citation(html_content, dump_citation, citation):
    text = json.dumps(dump_citation)
    return html_content.replace(citation, text)


# Saves a JSON file with the results of the page
def save_json(type, name, url, page):
    result = HTMLResult(url=url, content=page.content, statistic=page.statistic)
    path = "../data/result/" + type.lower() + "/" + name + ".json"
    with open(path, 'w') as outfile:
        json.dump(result, outfile, default=lambda o: o.__dict__, indent=4)
