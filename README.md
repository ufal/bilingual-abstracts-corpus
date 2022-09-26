# ÚFAL Bilingual Abstracts Corpus

A bilingual dataset of 2657 abstracts mostly between English and Czech.
TODO description 

You can download the dataset [here on Lindat](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-1731) or directly from the command-line:

```
wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-1731/corpus.jsonl
```

## Replicating results

To replicate the results, simply put `authors.xml` and `publications.xml` to `data/` and run the `parse.py` script.
If you are also interested in links to SemanticScholar, you may get them by running `parse.py -ss` (please not much slower results).

You may also run `statistics.py` to show an overview of the generated file.
The results should look similar to:

```
TODO
```