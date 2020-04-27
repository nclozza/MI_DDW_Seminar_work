import json
import re
import sys

from configuration import XML_FOLDER_PATH, XML_EXTENSION

sys.path.append("../")
from common.configuration import *
from common.object import Object
from common.util import get_urls, get_name_from_url, generate_url_from_name, save_file, windows_name_accepted

from general_configuration import XML_DUMP_PATH, RUNNING_ON_WINDOWS

PAGE_START_TAG = "<page>"
PAGE_END_TAG = "</page>"
TITLE_START_TAG = "<title>"
TITLE_END_TAG = "</title>"
REDIRECT_START_TAG = "<redirect title="


def save_file_from_array(filename, array):
    urls = [generate_url_from_name(x) for x in array]
    json_urls = Object()
    setattr(json_urls, "urls", urls)
    json_urls = json.dumps(json_urls, default=lambda o: o.__dict__)
    save_file(filename, json_urls)


def save_content_in_file(title, page_string):
    file_path = XML_FOLDER_PATH + title + XML_EXTENSION

    if len(file_path) >= 255:
        f = open("file_name_too_long.txt", "w")
        f.write(title)
        f.close()
        return False

    print("Title founded: " + title)
    with open(file_path, "w") as f:
        f.write(page_string)
        f.close()

    return True


titles_required_city = [get_name_from_url(string) for string in get_urls(CITY)]
titles_required_sport = [get_name_from_url(string) for string in get_urls(SPORT)]
titles_required_musical_artist = [get_name_from_url(string) for string in get_urls(MUSICAL_ARTIST)]

city_filenames_array = []
sport_filenames_array = []
musical_artist_filenames_array = []
with open("../" + XML_DUMP_PATH) as infile:
    page_string = ""
    in_page = False
    for line in infile:
        if not (titles_required_city and titles_required_sport and titles_required_musical_artist):
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

                if RUNNING_ON_WINDOWS and not windows_name_accepted(title):
                    continue

                if title in titles_required_city:
                    titles_required_city.remove(title)
                    city_filenames_array.append(title)
                    if not save_content_in_file(title, page_string):
                        continue

                elif title in titles_required_sport:
                    titles_required_sport.remove(title)
                    sport_filenames_array.append(title)
                    if not save_content_in_file(title, page_string):
                        continue

                elif title in titles_required_musical_artist:
                    titles_required_musical_artist.remove(title)
                    musical_artist_filenames_array.append(title)
                    if not save_content_in_file(title, page_string):
                        continue

            page_string = ""

save_file_from_array(AVAILABLE_URLS_CITY, city_filenames_array)
save_file_from_array(AVAILABLE_URLS_SPORT, sport_filenames_array)
save_file_from_array(AVAILABLE_URLS_MUSICAL_ARTIST, musical_artist_filenames_array)
