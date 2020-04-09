import json
import re

from src.DumpCrawler.configuration import XML_FOLDER_PATH, XML_EXTENSION, XML_DUMP_PATH
from src.common.configuration import *
from src.common.object import Object
from src.common.util import get_urls, get_name_from_url, generate_url_from_name, save_file

PAGE_START_TAG = "<page>"
PAGE_END_TAG = "</page>"
TITLE_START_TAG = "<title>"
TITLE_END_TAG = "</title>"
REDIRECT_START_TAG = "<redirect title="

titles_required_city = get_urls(CITY)
titles_required_sport = get_urls(SPORT)
titles_required_musical_artist = get_urls(MUSICAL_ARTIST)
titles_required = titles_required_city + titles_required_sport + titles_required_musical_artist

titles_required = [get_name_from_url(string) for string in titles_required]

filenames_array = []
with open(XML_DUMP_PATH) as infile:
    page_string = ""
    in_page = False
    for line in infile:
        if not titles_required:
            print("All titles required already founded")
            break

        if PAGE_START_TAG in line:
            in_page = True

        if in_page:
            page_string += line

        if PAGE_END_TAG in line:
            in_page = False

        if not in_page and len(page_string) > 0:
            if REDIRECT_START_TAG not in page_string:
                title = re.search(TITLE_START_TAG + '(.*)' +
                                  TITLE_END_TAG, page_string)

                title = title.group(1).replace("/", "_")
                file_path = XML_FOLDER_PATH + title + XML_EXTENSION

                if title in titles_required:
                    print("Title founded: " + title)
                    titles_required.remove(title)
                    filenames_array.append(title)

                    if len(file_path) >= 255:
                        f = open("file_name_too_long.txt", "w")
                        f.write(title)
                        f.close()
                        continue

                    with open(file_path, "w") as f:
                        f.write(page_string)
                        f.close()

            page_string = ""

urls = [generate_url_from_name(x) for x in filenames_array]
json_urls = Object()
setattr(json_urls, "urls", urls)
json_urls = json.dumps(json_urls, default=lambda o: o.__dict__)
save_file(AVAILABLE_URLS_IN_DUMP, json_urls)
