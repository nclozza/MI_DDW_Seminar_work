from time import sleep
import re

PAGE_START_TAG = "<page>"
PAGE_END_TAG = "</page>"
TITLE_START_TAG = "<title>"
TITLE_END_TAG = "</title>"
REDIRECT_START_TAG = "<redirect title="

with open("../../../enwiki-20200201-pages-articles-multistream1.xml-p10p30302") as infile:
    page_string = ""
    in_page = False
    for line in infile:
        if(PAGE_START_TAG in line):
            in_page = True

        if(in_page):
            page_string += line

        if(PAGE_END_TAG in line):
            in_page = False

        if(not in_page and len(page_string) > 0):
            if(REDIRECT_START_TAG not in page_string):
                title = re.search(TITLE_START_TAG + '(.*)' +
                                  TITLE_END_TAG, page_string)

                title = title.group(1).replace("/", "_")
                with open("pages/" + title + ".xml", "w") as f:
                    f.write(page_string)
                    f.close()

            page_string = ""
