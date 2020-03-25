def get_name_from_url(url):
    return url[url.rfind('/') + 1:]


def get_mili_time_diff(initial_time, final_time):
    time_diff = final_time - initial_time
    return int(time_diff.total_seconds() * 1000)
