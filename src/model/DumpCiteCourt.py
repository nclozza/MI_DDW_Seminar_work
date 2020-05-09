import sys

sys.path.append("../")
from model.DumpCite import DumpCite


class DumpCiteCourt(DumpCite):
    def __init__(self, litigants="", vol="", reporter="", opinion="", pinpoint="", court="", date="", url="",
                 accessdate="", quote=""):
        self.citetype = "court"
        self.litigants = litigants
        self.vol = vol
        self.reporter = reporter
        self.opinion = opinion
        self.pinpoint = pinpoint
        self.court = court
        self.date = date
        self.url = url
        self.accessdate = accessdate
        self.quote = quote
