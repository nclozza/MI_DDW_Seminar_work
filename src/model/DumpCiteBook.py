from src.model.DumpCite import DumpCite


class DumpCiteBook(DumpCite):
    def __init__(self, last1="", first1="", authorlink1="", authormask1="", last2="", first2="", displayauthors="",
                 lastauthoramp="", translatorlast1="", translatorfirst1="", translatorlink1="", translatormask1="",
                 date="", year="", origyear="", chapter="", scriptchapter="", transchapter="", chapterurl="",
                 chapterformat="", editor1last="", editor1first="", editor1link="", editor1mask="", displayeditors="",
                 title="", scripttitle="", transtitle="", url="", urlstatus="", format="", type="", series="",
                 language="", volume="", others="", edition="", location="", publisher="", publicationdate="", page="",
                 pages="", at="", nopp="", arxiv="", asin="", bibcode="", doi="", doibrokendate="", isbn="", issn="",
                 jfm="", jstor="", lccn="", mr="", oclc="", ol="", osti="", pmc="", pmid="", rfc="", ssrn="", zbl="",
                 id="", archiveurl="", archivedate="", accessdate="", via="", registration="", subscription="",
                 laysummary="", laysource="", laydate="", quote="", namelistformat="", mode="", postscript="", ref=""):
        self.citetype = "book"
        self.last1 = last1
        self.first1 = first1
        self.authorlink1 = authorlink1
        self.authormask1 = authormask1
        self.last2 = last2
        self.first2 = first2
        self.displayauthors = displayauthors
        self.lastauthoramp = lastauthoramp
        self.translatorlast1 = translatorlast1
        self.translatorfirst1 = translatorfirst1
        self.translatorlink1 = translatorlink1
        self.translatormask1 = translatormask1
        self.date = date
        self.year = year
        self.origyear = origyear
        self.chapter = chapter
        self.scriptchapter = scriptchapter
        self.transchapter = transchapter
        self.chapterurl = chapterurl
        self.chapterformat = chapterformat
        self.editor1last = editor1last
        self.editor1first = editor1first
        self.editor1link = editor1link
        self.editor1mask = editor1mask
        self.displayeditors = displayeditors
        self.title = title
        self.scripttitle = scripttitle
        self.transtitle = transtitle
        self.url = url
        self.urlstatus = urlstatus
        self.format = format
        self.type = type
        self.series = series
        self.language = language
        self.volume = volume
        self.others = others
        self.edition = edition
        self.location = location
        self.publisher = publisher
        self.publicationdate = publicationdate
        self.page = page
        self.pages = pages
        self.at = at
        self.nopp = nopp
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
        self.archiveurl = archiveurl
        self.archivedate = archivedate
        self.accessdate = accessdate
        self.via = via
        self.registration = registration
        self.subscription = subscription
        self.laysummary = laysummary
        self.laysource = laysource
        self.laydate = laydate
        self.quote = quote
        self.namelistformat = namelistformat
        self.mode = mode
        self.postscript = postscript
        self.ref = ref
