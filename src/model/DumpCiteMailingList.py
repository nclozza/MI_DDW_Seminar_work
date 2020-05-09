import sys

sys.path.append("../")
from model.DumpCite import DumpCite


class DumpCiteMailingList(DumpCite):
    def __init__(self, url="", title="", date="", accessdate="", mailinglist="", last="", first="", author="",
                 authorlink="", language="", quote="", archiveurl="", archivedate="", ref=""):
        self.citetype = "mailing list"
        self.url = url
        self.title = title
        self.date = date
        self.accessdate = accessdate
        self.mailinglist = mailinglist
        self.last = last
        self.first = first
        self.author = author
        self.authorlink = authorlink
        self.language = language
        self.quote = quote
        self.archiveurl = archiveurl
        self.archivedate = archivedate
        self.ref = ref
