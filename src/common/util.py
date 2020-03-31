import datetime
import json
import time

import src.common.url_type as url_type


def get_name_from_url(url):
    return url[url.rfind('/') + 1:]


def get_mili_time_diff(initial_time, final_time):
    time_diff = final_time - initial_time
    return int(time_diff.total_seconds() * 1000)


def wait_crawl_delay(initial_time, crawl_delay):
    final_time = datetime.datetime.now()
    time_diff = get_mili_time_diff(initial_time, final_time)

    if time_diff < crawl_delay:
        time.sleep((crawl_delay - time_diff) / 1000)


def get_urls(value):
    path = ""
    url_array = []

    if value == url_type.DEBUG:
        path = "../URL/debug.json"
    elif value == url_type.CITY:
        path = "../URL/city.json"

    if path != "":
        with open(path) as f:
            data = json.load(f)

        for url in data["results"]["bindings"]:
            url_array.append(url["url"]["value"])

    return url_array
