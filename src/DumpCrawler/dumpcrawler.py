import re
from DumpCiteBook import DumpCiteBook
from DumpCiteWeb import DumpCiteWeb

CITE_START = "{{cite "
CITE_END = "}}"

CITE_TYPES = ["book", "web"]


def get_cite_type(string):
    for cite_type in CITE_TYPES:
        if re.match("^" + cite_type + "(.*)", string, re.IGNORECASE):
            return cite_type


def create_cite_type_object(cite_type, string):
    ret = None
    if (cite_type == "book"):
        ret = DumpCiteBook()

    elif (cite_type == "web"):
        ret = DumpCiteWeb()

    else:
        # DEBUG
        # print(string)
        return

    array = string.split("|")

    # Cite type in the first element
    del array[0]
    for element in array:
        atr_name = re.findall('(.*?)=', element)
        if (atr_name):
            atr_name = atr_name[0]

            atr_value = re.findall(atr_name + '=(.*)', element)
            if (atr_value):
                atr_value = atr_value[0]
                setattr(ret, atr_name.replace("-", ""), atr_value.strip())
    # DEBUG
    ret.print()
    return ret


def remove_string_leftovers(string):
    quantity = 0
    for i in range(0, len(string) - 1):
        if (string[i] + string[i+1] == CITE_END):
            if (quantity > 0):
                quantity -= 1
            else:
                return string[:i]

        if (string[i] + string[i+1] == "{{"):
            quantity += 1

    return None


try:
    file = open("./pages/Prague.xml", "r")
    file_string = file.read()
    references = re.split(CITE_START, file_string, flags=re.IGNORECASE)

    # The first element contains the text before the first appearance of CITE_START
    del references[0]

    for line in references:
        string = remove_string_leftovers(line)

        if string:
            cite_type = get_cite_type(string)
            create_cite_type_object(cite_type, string)

except IOError as identifier:
    print(identifier)
