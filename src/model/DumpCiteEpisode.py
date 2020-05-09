import sys

sys.path.append("../")
from model.DumpCite import DumpCite


class DumpCiteEpisode(DumpCite):
    def __init__(self, title="", episodelink="", url="", accessdate="", series="", serieslink="", first="", last="",
                 network="", station="", date="", season="", seriesno="", number="", minutes="", time="", transcript="",
                 transcripturl="", quote="", language=""):
        self.citetype = "episode"
        self.title = title
        self.episodelink = episodelink
        self.url = url
        self.accessdate = accessdate
        self.series = series
        self.serieslink = serieslink
        self.first = first
        self.last = last
        self.network = network
        self.station = station
        self.date = date
        self.season = season
        self.seriesno = seriesno
        self.number = number
        self.minutes = minutes
        self.time = time
        self.transcript = transcript
        self.transcripturl = transcripturl
        self.quote = quote
        self.language = language
