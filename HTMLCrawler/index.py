import citation

from common.object import Object

user_agent = "DDW"
headers = {'User-Agent': user_agent}
urls = ["https://en.wikipedia.org/wiki/Paris", "https://en.wikipedia.org/wiki/Prague",
        "https://en.wikipedia.org/wiki/Budapest"]

citations = Object()

citation.get_all(urls, citations, headers)
