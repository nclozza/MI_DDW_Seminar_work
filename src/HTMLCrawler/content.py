def extract_text(soup, name):
    try:
        text_content = soup.find("div", {"id": "mw-content-text"})
        content = text_content.find_all(["p", "h2", "h3", "h4"])

        text = name + "\n"
        for index, elem in enumerate(content):
            if elem.name == "p":
                text += elem.text
            elif len(content) != index + 1:
                next_elem = content[(index + 1)]
                if next_elem.name == "p":
                    title = elem.find("span", {"class": "mw-headline"})
                    text += "\n" + title.text + "\n"

        return text
    except Exception as e:
        print(e)
