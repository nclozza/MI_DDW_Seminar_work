from pprint import pprint


class DumpCiteWeb:
    def __init__(self, url="", urlaccess="", title="", last="", first="",
                 authorlink="", last2="", first2="", authorlink2="", date="",
                 year="", origyear="", editorlast="", editorfirst="", editorlink="",
                 editor2last="", editor2first="", editor2link="", department="",
                 website="", series="", publisher="", agency="", location="", page="",
                 pages="", at="", language="", scripttitle="", transtitle="", type="",
                 format="", arxiv="", asin="", bibcode="", doi="", doibrokendate="",
                 isbn="", issn="", jfm="", jstor="", lccn="", mr="", oclc="", ol="",
                 osti="", pmc="", pmid="", rfc="", ssrn="", zbl="", id="", accessdate="",
                 urlstatus="", archiveurl="", archivedate="", via="", quote="", ref="",
                 postscript=""):
        self.url = url
        self.urlaccess = urlaccess
        self.title = title
        self.last = last
        self.first = first
        self.authorlink = authorlink
        self.last2 = last2
        self.first2 = first2
        self.authorlink2 = authorlink2
        self.date = date
        self.year = year
        self.origyear = origyear
        self.editorlast = editorlast
        self.editorfirst = editorfirst
        self.editorlink = editorlink
        self.editor2last = editor2last
        self.editor2first = editor2first
        self.editor2link = editor2link
        self.department = department
        self.website = website
        self.series = series
        self.publisher = publisher
        self.agency = agency
        self.location = location
        self.page = page
        self.pages = pages
        self.at = at
        self.language = language
        self.scripttitle = scripttitle
        self.transtitle = transtitle
        self.type = type
        self.format = format
        self.arxiv = arxiv
        self.asin = asin
        self.bibcode = bibcode
        self.doi = doi
        self.doibrokendate = doibrokendate
        self.isbn = isbn
        self.issn = issn
        self.jfm = jfm
        self.jstor = jstor
        self.lccn = lccn
        self.mr = mr
        self.oclc = oclc
        self.ol = ol
        self.osti = osti
        self.pmc = pmc
        self.pmid = pmid
        self.rfc = rfc
        self.ssrn = ssrn
        self.zbl = zbl
        self.id = id
        self.accessdate = accessdate
        self.urlstatus = urlstatus
        self.archiveurl = archiveurl
        self.archivedate = archivedate
        self.via = via
        self.quote = quote
        self.ref = ref
        self.postscript = postscript

    def print(self):
        pprint(vars(self))
