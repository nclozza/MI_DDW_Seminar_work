from src.model.HTMLCitation import HTMLCitation
from src.model.HTMLReference import HTMLReference


class HTMLPage:
    def __init__(self):
        self.citation = HTMLCitation()
        self.reference = HTMLReference()
