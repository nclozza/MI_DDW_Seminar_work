import sys

sys.path.append("../")
from model.HTMLCitationType import HTMLCitationType


class HTMLStatistic:
    def __init__(self):
        self.total_citations_in_HTML = 0
        self.total_citations_in_dump = 0
        self.total_citations_in_dump_per_type = HTMLCitationType()
        self.citations_matched = 0
        self.citations_matched_per_type = HTMLCitationType()
