import sys

sys.path.append("../")
from model.DumpCite import DumpCite


class DumpCiteEncyclopedia(DumpCite):
    def __init__(self, last="", first="", authorlink="", editorlast="", editorfirst="", editorlink="", encyclopedia="",
                 title="", transtitle="", url="", accessdate="", language="", edition="", date="", year="",
                 publisher="", series="", volume="", location="", id="", isbn="", oclc="", doi="", pages="",
                 archiveurl="", archivedate="", urlstatus="", quote="", ref=""):
        self.citetype = "encyclopedia"
        self.last = last
        self.first = first
        self.authorlink = authorlink
        self.editorlast = editorlast
        self.editorfirst = editorfirst
        self.editorlink = editorlink
        self.encyclopedia = encyclopedia
        self.title = title
        self.transtitle = transtitle
        self.url = url
        self.accessdate = accessdate
        self.language = language
        self.edition = edition
        self.date = date
        self.year = year
        self.publisher = publisher
        self.series = series
        self.volume = volume
        self.location = location
        self.id = id
        self.isbn = isbn
        self.oclc = oclc
        self.doi = doi
        self.pages = pages
        self.archiveurl = archiveurl
        self.archivedate = archivedate
        self.urlstatus = urlstatus
        self.quote = quote
        self.ref = ref
