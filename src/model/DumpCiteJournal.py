import sys

sys.path.append("../")
from model.DumpCite import DumpCite


class DumpCiteJournal(DumpCite):
    def __init__(self, last1="", first1="", authorlink1="", last2="", first2="", authorlink2="", last3="", first3="",
                 authorlink3="", last4="", first4="", authorlink4="", last5="", first5="", authorlink5="",
                 displayauthors="", authormask="", namelistformat="", lastauthoramp="", date="", year="", origyear="",
                 editor1last="", editor1first="", editor1link="", editor2last="", editor2first="", editor2link="",
                 editor3last="", editor3first="", editor3link="", editor4last="", editor4first="", editor4link="",
                 editor5last="", editor5first="", editor5link="", displayeditors="", others="", title="",
                 scripttitle="", transtitle="", url="", urlstatus="", format="", urlaccess="", department="",
                 journal="", type="", series="", language="", edition="", location="", publisher="",
                 publicationplace="", publicationdate="", volume="", issue="", page="", pages="", at="", nopp="",
                 arxiv="", asin="", bibcode="", biorxiv="", citeseerx="", doi="", doibrokendate="", doiaccess="",
                 isbn="", issn="", jfm="", jstor="", jstoraccess="", lccn="", mr="", oclc="", ol="", olaccess="",
                 osti="", ostiaccess="", pmc="", pmid="", rfc="", ssrn="", zbl="", id="", archiveurl="", archivedate="",
                 accessdate="", via="", registration="", subscription="", layurl="", laysource="", laydate="", quote="",
                 postscript="", ref=""):
        self.citetype = "journal"
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
        self.others = others
        self.title = title
        self.scripttitle = scripttitle
        self.transtitle = transtitle
        self.url = url
        self.urlstatus = urlstatus
        self.format = format
        self.urlaccess = urlaccess
        self.department = department
        self.journal = journal
        self.type = type
        self.series = series
        self.language = language
        self.edition = edition
        self.location = location
        self.publisher = publisher
        self.publicationplace = publicationplace
        self.publicationdate = publicationdate
        self.volume = volume
        self.issue = issue
        self.page = page
        self.pages = pages
        self.at = at
        self.nopp = nopp
        self.arxiv = arxiv
        self.asin = asin
        self.bibcode = bibcode
        self.biorxiv = biorxiv
        self.citeseerx = citeseerx
        self.doi = doi
        self.doibrokendate = doibrokendate
        self.doiaccess = doiaccess
        self.isbn = isbn
        self.issn = issn
        self.jfm = jfm
        self.jstor = jstor
        self.jstoraccess = jstoraccess
        self.lccn = lccn
        self.mr = mr
        self.oclc = oclc
        self.ol = ol
        self.olaccess = olaccess
        self.osti = osti
        self.ostiaccess = ostiaccess
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
        self.layurl = layurl
        self.laysource = laysource
        self.laydate = laydate
        self.quote = quote
        self.postscript = postscript
        self.ref = ref
