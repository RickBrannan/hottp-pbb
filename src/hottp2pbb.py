"""
    convert hottp.xml into two different PBB files,
    one for English and one for French
    RWB 2023-12-08
"""
import os
import dataclasses
import json
import regex as re
import pandas as pd
from hebrew import Hebrew
from docx import Document
from unicodedata import normalize
from biblelib.word import BCVWPID, BCVID, fromusfm
from lxml import etree
# from shared.shared_classes import *
from src import DATAPATH, ROOT


@dataclasses.dataclass
class Word:
    identifier: str
    text: str
    after: str
    gloss: str
    pos: str

@dataclasses.dataclass
class Verse:
    identifier: str
    book: str
    chapter: str
    verse: str
    usfm: str
    # the str is the Word.identifier so we can sort to ensure word order
    words: dict[str, Word] = dataclasses.field(default_factory=list)


hottp_dir = ROOT.parent.parent / "ubsicap/ubs-open-license/HOTTP/"
data_dir = DATAPATH / "pbb/"
macula_hebrew_nodes_dir = ROOT.parent.parent / "Clear/macula-hebrew/Nodes/"
macula_hebrew_mappings = ROOT.parent.parent / "Clear/macula-hebrew/mappings/morpheme-mappings.xml"

lang = "en"
# lang = "fr"

# load hebrew word information from Clear-Bible's macula-hebrew data
def load_wlc_lines():
    print(f"Loading WLC from Nodes")
    return_lines = {}
    previous_verse_id = "01001001"
    current_verse_id = ""
    words = {}

    for filename in os.listdir(macula_hebrew_nodes_dir):
        if filename == "macula-hebrew.xml":
            continue
        if filename.endswith(".xml"):
            macula_xml = etree.parse(macula_hebrew_nodes_dir / filename)
            macula_root = macula_xml.getroot()
            for item in macula_root.xpath(".//*[@xml:id]"):
                identifier = item.attrib['{http://www.w3.org/XML/1998/namespace}id']
                # identifier = re.sub(r"^o", "", identifier)
                if re.search(r"[^o0-9]", identifier):
                    # blasted hebrew-prepended id whatever thingies
                    continue
                bcv = BCVWPID(identifier)
                # create the verse object if it doesn't exist
                current_verse_id = bcv.book_ID + bcv.chapter_ID + bcv.verse_ID
                if previous_verse_id != current_verse_id:
                    # we need to dump verse info.
                    previous_bcv = BCVID(previous_verse_id)
                    return_lines[previous_verse_id] = Verse(previous_verse_id, previous_bcv.book_ID, previous_bcv.chapter_ID,
                                                            previous_bcv.verse_ID, previous_bcv.to_usfm(), words)
                    previous_verse_id = current_verse_id
                    words = {}
                    alt_id_counter = {}
                # create the word object
                after = ""
                if item.attrib.__contains__("after"):
                    after = item.attrib["after"]
                english = ""
                if item.attrib.__contains__("english"):
                    english = item.attrib["english"]
                pos = ""
                if item.attrib.__contains__("pos"):
                    pos = item.attrib["pos"]
                word = Word(identifier, item.text, after, english, pos)
                heb = Hebrew(item.text)
                word.text = heb.no_taamim().string
                words[word.identifier] = word

    bcv = BCVID(current_verse_id)
    return_lines[current_verse_id] = Verse(current_verse_id, bcv.book_ID, bcv.chapter_ID, bcv.verse_ID, bcv.to_usfm(), words)

    # send it back
    return return_lines


# the morpheme-mappings.xml allows mapping from the MARBLE word identifiers
# used in UBSICAP to the macula word identifiers used in Clear-Bible's macula-hebrew
# this will allow us to get the word-level data for the references specified in HOTTP
def load_morpheme_mappings():
    print(f"Loading morpheme mappings from {macula_hebrew_mappings}")
    morpheme_mappings = {}
    morpheme_xml = etree.parse(macula_hebrew_mappings)
    morpheme_root = morpheme_xml.getroot()
    for item in morpheme_root.xpath(".//m"):
        morpheme_mappings[item.attrib["marble"]] = "o" + item.attrib["n"]
    return morpheme_mappings


def get_hebrew_heading(entry):
    hebrew_text = []
    for reference in entry.xpath(".//Reference"):
        marble_id = reference.text
        if marble_id in morpheme_mappings:
            macula_id = morpheme_mappings[marble_id]
            # bcv = BCVWPID(re.sub(r"^o", "", macula_id))
            bcv = BCVWPID(macula_id)
            if macula_id in wlc_lines[bcv.to_bcvid].words:
                word = wlc_lines[bcv.to_bcvid].words[macula_id]
                hebrew_text.append(word)
            else:
                print(f"WARNING: {macula_id} not found in WLC")

    # build the Hebrew string
    return_hebrew = ""
    for word in hebrew_text:
        return_hebrew += word.text + word.after

    return return_hebrew


def get_current_reference(entry):
    refs = []
    for reference in entry.xpath(".//Reference"):
        marble_id = reference.text
        if marble_id in morpheme_mappings:
            macula_id = morpheme_mappings[marble_id]
            bcv = BCVWPID(re.sub(r"^o", "", macula_id))
            if not bcv.to_bcvid in refs:
                refs.append(bcv.to_bcvid)

    if len(refs) == 1:
        return BCVID(refs[0]).to_usfm()
    else:
        return f"{BCVID(refs[0]).to_usfm()}–{int(BCVID(refs[-1]).verse_ID)}"


# preliminaries. load macula data
wlc_lines = load_wlc_lines()
morpheme_mappings = load_morpheme_mappings()

# get a word doc started since that's what PBB uses
pbb_doc = Document()

# title page? maybe later

# open HOTTP.XML and start parsin'.
hottp_xml = etree.parse(hottp_dir / "hottp.xml")
hottp_root = hottp_xml.getroot()
for entry in hottp_root.xpath(".//HOTTP_Entry"):
    id = entry.attrib["Id"]
    hebrew_heading = get_hebrew_heading(entry)
    current_reference = get_current_reference(entry)
    print(f"{id}: {hebrew_heading} {current_reference}")

