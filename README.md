# Mining Wikipedia Content

## Seminar work - Web Data Mining

---

### Requirements

- Python 3
- [Download a XML Dump](https://dumps.wikimedia.org) - Tested with [this dump](https://dumps.wikimedia.org/enwiki/20200201/enwiki-20200201-pages-articles-multistream.xml.bz2)
- Clone the repository

```
> git clone https://github.com/nclozza/MI_DDW_Seminar_work.git
> cd MI_DDW_Seminar_work
```

### General configuration

- To specify new URLs to mine, first generate the proper JSON using [this site](http://dbpedia.org/sparql) with the format specified in `src/query`
- For more configurations, please edit the file `src/general_configuration.py`

### Modules description

- **XML Dump Splitter:** Splits the whole dump into small _.xml_ files, each one with the name of the page title
- **Dump Crawler:** Extracts all the references from the available dumps (the ones that were generated with the XML Dump Splitter) and generates a JSONL with the structured references for each different page
- **HTML Crawler:** Extracts all the citations from the HTML (directly from the website), does the match between those citations and the references from the JSONLs, and generates a JSON with all the page content, replacing the citations with the references

### Output

The output of this project is a JSON file per each website mined that is specified in the files from `src/data/dbpedia` and is also available in the dump
The outputs are stored in `src/data/result`

---

### Linux (Tested on Ubuntu 18.04 and 20.04)

#### Install packages

```
> pip3 install -r requirements.txt
```

#### Run XML Dump Splitter

```
> cd src/DumpCrawler
> python3 xml_splitter.py
```

#### Run Dump Crawler

```
> cd src/DumpCrawler
> python3 dump_crawler.py
```

#### Run HTML Crawler

```
> cd src/HTMLCrawler
> python3 HTML_crawler.py
```

---

### Windows

#### Install packages

```
> python -m pip install -r requirements.txt
```

#### Run XML Dump Splitter

```
> cd src/DumpCrawler
> python xml_splitter.py
```

#### Run Dump Crawler

```
> cd src/DumpCrawler
> python dump_crawler.py
```

#### Run HTML Crawler

```
> cd src/HTMLCrawler
> python HTML_crawler.py
```
