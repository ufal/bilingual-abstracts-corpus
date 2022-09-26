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
Language distribution: [('en', 2086), ('cs', 548), ('ru', 13), ('de', 4), ('sk', 2), ('dsb', 2), ('fr', 1), ('lt', 1)]
```
