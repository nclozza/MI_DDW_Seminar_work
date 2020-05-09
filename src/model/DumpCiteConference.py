import sys

sys.path.append("../")
from model.DumpCite import DumpCite


class DumpCiteConference(DumpCite):
    def __init__(self, url="", title="", first="", last="", author="", authorlink="", date="", year="", conference="",
                 conferenceurl="", editor="", others="", volume="", edition="", booktitle="", publisher="",
                 archiveurl="", archivedate="", location="", pages="", format="", id="", isbn="", bibcode="", oclc="",
                 doi="", accessdate="", quote="", ref="", postscript="", language="", page="", at="", transtitle=""):
        self.citetype = "conference"
        self.url = url
        self.title = title
        self.first = first
        self.last = last
        self.author = author
        self.authorlink = authorlink
        self.date = date
        self.year = year
        self.conference = conference
        self.conferenceurl = conferenceurl
        self.editor = editor
        self.others = others
        self.volume = volume
        self.edition = edition
        self.booktitle = booktitle
        self.publisher = publisher
        self.archiveurl = archiveurl
        self.archivedate = archivedate
        self.location = location
        self.pages = pages
        self.format = format
        self.id = id
        self.isbn = isbn
        self.bibcode = bibcode
        self.oclc = oclc
        self.doi = doi
        self.accessdate = accessdate
        self.quote = quote
        self.ref = ref
        self.postscript = postscript
        self.language = language
        self.page = page
        self.at = at
        self.transtitle = transtitle
