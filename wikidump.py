#!/usr/bin/env python
import xml.etree.ElementTree as ET
import ipdb

it = ET.iterparse("full_data/simplewiki.xml")

tagprefix = "{http://www.mediawiki.org/xml/export-0.10/}"


class Ctx:
    def __init__(self):
        self.idx = 0

    def fname(self, page):
        return f"full_data/articles/article_{self.idx}.txt"


def main():
    ctx = Ctx()
    for _, el in it:
        if tag(el) == "page":
            page = process_page(el)
            if not page:
                continue
            save_page(ctx, page)
            ctx.idx += 1


def tag(el):
    return el.tag[len(tagprefix):]


def process_page(el):
    title = None
    text = None
    for c in el.iter():
        t = tag(c)
        if tag(c) == "title":
            title = c.text
        elif tag(c) == "text":
            text = c.text
    if title is None or text is None or len(text.split()) <= 5:
        print(f"warn: title={title} text={text}")
        return False
    return (title, text)


def save_page(ctx, page):
    title, text = page
    with open(ctx.fname(page), "w") as f:
        f.write(title)
        f.write("\n")
        f.write(text)

main()
