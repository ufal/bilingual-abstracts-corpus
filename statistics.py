#!/usr/bin/env python3

import json
import numpy as np
from tqdm import tqdm
import argparse
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

args = argparse.ArgumentParser()
args.add_argument(
    "-d", "--data", default="data/corpus.jsonl"
)
args = args.parse_args()

with open(args.data, "r") as f:
    data = [json.loads(x) for x in f.readlines()]


sent_counts = []
word_counts = []
has_s2_url = []
langs = []

for record in tqdm(data):
    sent_counts.append(len(sent_tokenize(record["abstract_en"])))
    word_counts.append(len(word_tokenize(record["abstract_en"])))
    langs.append(record["lang"])
    has_s2_url.append("s2_url" in record)

print(
    "Total records:", len(data)
)
print(
    "Average sents (words) per abstract:",
    f"{np.average(sent_counts):.1f} ({np.average(word_counts):.1f})"
)
print(
    "Total sents (words) (en):",
    f"{sum(sent_counts)} ({sum(word_counts)})"
)
print("Langs:", ", ".join([
    f"{l} {v} ({v/len(langs):.1%})"
    for l, v in Counter(langs).most_common()
]))
print(
    "Papers with S2 link:",
    f"{np.average(has_s2_url):.1%}"
)