# ÚFAL Bilingual Abstracts Corpus

A bilingual dataset of 2657 abstracts mostly between English and Czech.
TODO description 

You can download the dataset [here on Lindat](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-1731) or directly from the command-line:

```
wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-1731/corpus.jsonl
```

## Replicating results

To replicate the results, simply put `authors.xml` and `publications.xml` to `data/` and run the `main.py` script.
If you are also interested in links to SemanticScholar, you may get them by running `main.py -ss` (expect much slower runtime).

The result of running the file should look close to:

```
Preprocessing authors
...
Processing main publication file
...
Total valid records: 2657
```

You can run `statistics.py` to get an overview for the dataset:

- **Average sents (words) per abstract**: 4.0 (96.0)
- **Total sents (words) (en)**:           11k (255k)
- **Langs**:                              en 2086 (78.5%), cs 548 (20.6%), ru 13 (0.5%), ... (long tail of less-represented languages)