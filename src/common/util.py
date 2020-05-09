import datetime
import json
import sys
import time
from os import listdir
from os.path import isfile, join

sys.path.append('../')
import common.configuration as configuration


# Returns the name of the wikipedia URL page
def get_name_from_url(url):
    return url[url.rfind('/') + 1:]


# Calculates the difference in miliseconds
def get_mili_time_diff(initial_time, final_time):
    time_diff = final_time - initial_time
    return int(time_diff.total_seconds() * 1000)


# Waits for the crawl delay only if the time passed is less than the crawl delay
def wait_crawl_delay(initial_time, crawl_delay):
    final_time = datetime.datetime.now()
    time_diff = get_mili_time_diff(initial_time, final_time)

    if time_diff < crawl_delay:
        time.sleep((crawl_delay - time_diff) / 1000)


# Returns the URLs obtained from dbpedia per category
def get_urls(value):
    path = ""
    url_array = []

    if value == configuration.CITY:
        path = "../data/dbpedia/city.json"
    elif value == configuration.SPORT:
        path = "../data/dbpedia/sport.json"
    elif value == configuration.MUSICAL_ARTIST:
        path = "../data/dbpedia/musical_artist.json"

    if path != "":
        with open(path) as f:
            data = json.load(f)

        for url in data["results"]["bindings"]:
            url_array.append(url["url"]["value"])

    return url_array


# Returns the URLs founded in the dumps per category
def get_available_urls(value):
    path = ""

    if value == configuration.CITY:
        path = configuration.AVAILABLE_URLS_CITY
    elif value == configuration.SPORT:
        path = configuration.AVAILABLE_URLS_SPORT
    elif value == configuration.MUSICAL_ARTIST:
        path = configuration.AVAILABLE_URLS_MUSICAL_ARTIST

    with open(path) as f:
        data = json.load(f)

    return data["urls"]


# Returns all the files from a specific path
def get_all_files_from_path(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


# Returns the wikipedia page URL from the name
def generate_url_from_name(name):
    return "http://en.wikipedia.org/wiki/" + name


# Saves a file
def save_file(filename, string):
    f = open(filename, 'w')
    f.write(string)
    f.close()


# Removes the extension of a file name
def remove_file_extension_from_name(file_name):
    return file_name[:file_name.rfind(".")]


# Checks for all the forbidden characters of a file name in Windows
def windows_name_accepted(string):
    return all((31 <= ord(c) <= 126 and c not in "<>:\"/\\|?*") for c in string)
