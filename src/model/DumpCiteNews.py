from src.model.DumpCite import DumpCite


class DumpCiteNews(DumpCite):
    def __init__(self, last1="", first1="", authorlink1="", last2="", first2="", authorlink2="", last3="", first3="",
                 authorlink3="", last4="", first4="", authorlink4="", last5="", first5="", authorlink5="",
                 displayauthors="", authormask="", namelistformat="", lastauthoramp="", date="", year="", origyear="",
                 title="", scripttitle="", transtitle="", url="", urlstatus="", format="", editor1last="",
                 editor1first="", editor1link="", editor2last="", editor2first="", editor2link="", editor3last="",
                 editor3first="", editor3link="", editor4last="", editor4first="", editor4link="", editor5last="",
                 editor5first="", editor5link="", displayeditors="", department="", work="", type="", series="",
                 language="", volume="", issue="", others="", edition="", location="", publisher="", publicationdate="",
                 agency="", page="", pages="", at="", nopp="", arxiv="", asin="", bibcode="", doi="", doibrokendate="",
                 isbn="", issn="", jfm="", jstor="", lccn="", mr="", oclc="", ol="", osti="", pmc="", pmid="", rfc="",
                 ssrn="", zbl="", id="", archiveurl="", archivedate="", accessdate="", via="", layurl="", laysource="",
                 laydate="", quote="", postscript="", ref=""):
        self.citetype = "news"
        self.last1 = last1
        self.first1 = first1
        self.authorlink1 = authorlink1
        self.last2 = last2
        self.first2 = first2
        self.authorlink2 = authorlink2
        self.last3 = last3
        self.first3 = first3
        self.authorlink3 = authorlink3
        self.last4 = last4
        self.first4 = first4
        self.authorlink4 = authorlink4
        self.last5 = last5
        self.first5 = first5
        self.authorlink5 = authorlink5
        self.displayauthors = displayauthors
        self.authormask = authormask
        self.namelistformat = namelistformat
        self.lastauthoramp = lastauthoramp
        self.date = date
        self.year = year
        self.origyear = origyear
        self.title = title
        self.scripttitle = scripttitle
        self.transtitle = transtitle
        self.url = url
        self.urlstatus = urlstatus
        self.format = format
        self.editor1last = editor1last
        self.editor1first = editor1first
        self.editor1link = editor1link
        self.editor2last = editor2last
        self.editor2first = editor2first
        self.editor2link = editor2link
        self.editor3last = editor3last
        self.editor3first = editor3first
        self.editor3link = editor3link
        self.editor4last = editor4last
        self.editor4first = editor4first
        self.editor4link = editor4link
        self.editor5last = editor5last
        self.editor5first = editor5first
        self.editor5link = editor5link
        self.displayeditors = displayeditors
        self.department = department
        self.work = work
        self.type = type
        self.series = series
        self.language = language
        self.volume = volume
        self.issue = issue
        self.others = others
        self.edition = edition
        self.location = location
        self.publisher = publisher
        self.publicationdate = publicationdate
        self.agency = agency
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
        self.layurl = layurl
        self.laysource = laysource
        self.laydate = laydate
        self.quote = quote
        self.postscript = postscript
        self.ref = ref
