import re
import sys
from xml.sax import saxutils as su

sys.path.append("../")
from configuration import *
from common.util import remove_file_extension_from_name, get_all_files_from_path, save_file
from model.DumpCiteBook import DumpCiteBook
from model.DumpCiteJournal import DumpCiteJournal
from model.DumpCiteNews import DumpCiteNews
from model.DumpCiteWeb import DumpCiteWeb
from model.DumpCiteConference import DumpCiteConference
from model.DumpCiteCourt import DumpCiteCourt
from model.DumpCiteEncyclopedia import DumpCiteEncyclopedia
from model.DumpCiteEpisode import DumpCiteEpisode
from model.DumpCiteMailingList import DumpCiteMailingList

from general_configuration import IGNORE_EXISTING_FILES

CITE_START = "{{cite "
CITE_END = "}}"


def get_cite_type(string):
    for cite_type in CITE_TYPES:
        if re.match("^" + cite_type + "(.*)", string, re.IGNORECASE):
            return cite_type


def custom_split(string, open_pair=("{", "(", "["), close_pair=("}", ")", "]"), separator="|"):
    ret = []
    brackets_count = 0
    character_count = 0
    last_pipe_index = 0

    for character in string:
        character_count += 1
        if character in open_pair:
            brackets_count += 1

        elif character in close_pair:
            brackets_count -= 1

        elif character in separator and brackets_count <= 0:
            ret.append(string[last_pipe_index:character_count - 1].strip())
            last_pipe_index = character_count

    ret.append(string[last_pipe_index:].strip())
    return ret


def convert_to_regular_HTML_and_delete_comments(string):
    string = su.unescape(string)
    return re.sub("(<!--.*?-->)", "", string, flags=re.DOTALL)


def create_cite_type_object(cite_type, string):
    string = convert_to_regular_HTML_and_delete_comments(string)
    ret = None
    if cite_type == "book":
        ret = DumpCiteBook()

    elif cite_type == "web":
        ret = DumpCiteWeb()

    elif cite_type == "news":
        ret = DumpCiteNews()

    elif cite_type == "journal":
        ret = DumpCiteJournal()

    elif cite_type == "conference":
        ret = DumpCiteConference()

    elif cite_type == "court":
        ret = DumpCiteCourt()

    elif cite_type == "encyclopedia":
        ret = DumpCiteEncyclopedia()

    elif cite_type == "episode":
        ret = DumpCiteEpisode()

    elif cite_type == "mailing list":
        ret = DumpCiteMailingList()

    else:
        # DEBUG
        # print(string)
        return

    array = custom_split(string)

    for element in array:
        atr_name = re.findall('(.*?)=', element)
        if atr_name:
            atr_name = atr_name[0]

            atr_value = re.findall(atr_name + '=(.*)', element)
            if atr_value:
                atr_value = atr_value[0]
                setattr(ret, atr_name.replace("-", ""), atr_value.strip())

    return ret


def remove_string_leftovers(string):
    quantity = 0
    for i in range(0, len(string) - 1):
        if string[i] + string[i + 1] == CITE_END:
            if quantity > 0:
                quantity -= 1
            else:
                return string[:i]

        if string[i] + string[i + 1] == "{{":
            quantity += 1

    return None


try:

    files_to_process = get_all_files_from_path(XML_FOLDER_PATH)
    files = files_to_process

    if IGNORE_EXISTING_FILES:
        files_to_process = {remove_file_extension_from_name(x) for x in files_to_process}

        files_processed = get_all_files_from_path(JSONL_FOLDER_PATH)
        files_processed = {remove_file_extension_from_name(x) for x in files_processed}

        files = [x for x in files_to_process if x not in files_processed]
        files = {x + XML_EXTENSION for x in files}

    files = ["Archery.xml"]

    for file_name in files:
        print("Processing: " + file_name)
        file = open(XML_FOLDER_PATH + file_name, "r")
        file_string = file.read()
        references = re.split(CITE_START, file_string, flags=re.IGNORECASE)

        # The first element contains the text before the first appearance of CITE_START
        del references[0]

        jsonl = ""
        for line in references:
            string = remove_string_leftovers(line)

            if string:
                cite_type = get_cite_type(string)
                cite_type_object = create_cite_type_object(cite_type, string)
                if cite_type_object:
                    jsonl += cite_type_object.to_json()
                    jsonl += "\n"

        save_file(JSONL_FOLDER_PATH + remove_file_extension_from_name(file_name) + JSONL_EXTENSION, jsonl)

except IOError as identifier:
    print(identifier)
