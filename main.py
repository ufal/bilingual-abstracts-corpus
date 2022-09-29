#!/usr/bin/env python3

import json
import re
from bs4 import BeautifulSoup
import semanticscholar
from tqdm import tqdm
import time
import argparse

ss = semanticscholar.SemanticScholar()
re_collapse_whitespace = re.compile(" +")

args = argparse.ArgumentParser()
args.add_argument(
    "-dp", "--data-publications", default="data/publications.xml"
)
args.add_argument(
    "-da", "--data-authors", default="data/authors.xml"
)
args.add_argument(
    "-do", "--data-out", default="data/corpus.jsonl"
)
args.add_argument(
    "-ss", "--semantic-scholar", action="store_true"
)
args = args.parse_args()

with open(args.data_publications, "r") as f:
    data_pub = BeautifulSoup(f.read(), "xml")

with open(args.data_authors, "r") as f:
    data_aut = BeautifulSoup(f.read(), "xml")

print("Preprocessing authors")
author_map = {}
for record in tqdm(list(data_aut.find_all("Record"))):
    name_first = record.find("Field", attrs={"Name": "FirstName"}).text
    name_middle = record.find("Field", attrs={"Name": "MiddleName"}).text
    name_last = record.find("Field", attrs={"Name": "LastName"}).text
    name_all = re_collapse_whitespace.sub(
        " ", f"{name_first} {name_middle} {name_last}")
    author_map[record["Id"]] = name_all

# clean up file
with open(args.data_out, "w"):
    pass
fout = open(args.data_out, "a")

LANG_MAP = {
    "cze": "cs",
    "eng": "en",
    "deu": "de",
    "ger": "de",
    "rus": "ru",
    "fre": "fr",
    "sla": "sk",
    "lit": "lt",
}

stored_titles = set()
stored_records = 0

print("Processing main publication file")
for record in tqdm(list(data_pub.find_all("Record"))):
    record_out = {}

    # extract information from the XML
    lang = record.find("Field", attrs={"Name": "Language"}).text
    year = record.find("Field", attrs={"Name": "Year"}).text
    abstract_cs = record.find("Field", attrs={"Name": "CzechAbstract"}).text
    abstract_en = record.find("Field", attrs={"Name": "EnglishAbstract"}).text
    abstract_orig = record.find(
        "Field", attrs={"Name": "OriginalLanguageAbstract"}
    ).text
    title_cs = record.find("Field", attrs={"Name": "CzechTitle"}).text
    title_en = record.find("Field", attrs={"Name": "EnglishTitle"}).text
    title_orig = record.find("Field", attrs={"Name": "Title"}).text
    authors = record.find("Field", attrs={"Name": "Author"}).text.split(";")

    title_hash = f"{title_en}|{title_cs}|{title_orig}|{authors}|{abstract_en}|{abstract_cs}|{abstract_orig}"
    if title_hash in stored_titles:
        continue
    stored_titles.add(title_hash)

    # map language to standard 2-char format
    if lang in LANG_MAP:
        lang = LANG_MAP[lang]

    record_out["lang"] = lang
    record_out["year"] = year

    # skip invalid language
    if lang == "":
        continue

    # if the title is unavailable, set it to the original
    if len(title_en) == 0 and lang == "en":
        title_en = title_orig
    elif len(title_cs) == 0 and lang == "cs":
        title_cs = title_orig

    # sometimes the fields are not filled properly
    if len(abstract_cs) == 0 and lang == "cs":
        abstract_cs = abstract_orig
    elif len(abstract_en) == 0 and lang == "en":
        abstract_en = abstract_orig

    # if we don't have at least two abstracts, skip
    if sum([len(abstract_en) == 0, len(abstract_cs) == 0, len(abstract_orig) == 0]) >= 2:
        continue

    record_out["title_en"] = title_en.strip()
    record_out["title_cs"] = title_cs.strip()
    if lang not in {"en", "cs"}:
        record_out[f"title_{lang}"] = title_orig.strip()

    record_out["abstract_en"] = abstract_en.strip()
    record_out["abstract_cs"] = abstract_cs.strip()
    if lang not in {"en", "cs"}:
        record_out[f"abstract_{lang}"] = abstract_orig.strip()

    record_out["authors"] = [author_map[a_id] for a_id in authors]

    if args.semantic_scholar:
        title_en_hash = "".join([c for c in title_en.lower() if c.isalpha()])
        for paper_other in ss.search_paper(title_en):
            title_hash_other = "".join(
                [c for c in paper_other["title"].lower() if c.isalpha()])
            if title_hash_other == title_en_hash:
                print(
                    "Found a matching paper!",
                    title_hash_other, title_en_hash
                )
                record_out["SemanticScholar_paperId"] = paper_other["paperId"]
                break

        # delay to not trigger throttle
        # by default 100 per 5 minutes -> 20 per minute -> 3 per second
        time.sleep(3.5)

    fout.write(json.dumps(record_out, ensure_ascii=False) + "\n")
    stored_records += 1

print("Total valid records:", stored_records)
