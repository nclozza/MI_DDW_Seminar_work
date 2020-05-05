import sys

sys.path.append("../")
from model.HTMLStatistic import HTMLStatistic


class HTMLPage:
    def __init__(self):
        self.citations = []
        self.content = ""
        self.statistic = HTMLStatistic()
