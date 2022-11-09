# ÚFAL Bilingual Abstracts Corpus

A bilingual dataset of 2657 abstracts mostly between English and Czech from researchers at the [Institute of Formal and Applied Linguistics](https://ufal.mff.cuni.cz/), Charles University in Prague.
You can download the dataset [here on Lindat](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-1731) or directly from the command-line:

```
wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-1731/corpus.jsonl
```

## Replicating results

To replicate the results, simply put `authors.xml` and `publications.xml` to `data/` and run the `main.py` script.
If you are also interested in links to SemanticScholar, you may get them by running `main.py -s2` (expect much slower runtime).

You can run `statistics.py` to get an overview for the dataset:

- **Average sents (words) per abstract**: 4.0 (96.0)
- **Total sents (words) (en)**:           11k (255k)
- **Langs**:                              en 2086 (78.5%), cs 548 (20.6%), ru 13 (0.5%), ... (long tail of less-represented languages)
- **Papers with S2 links**:              43.1%

## Example

```
{
    "lang": "en", "year": "2022",
    "title_en": "CorefUD 1.0: Coreference Meets Universal Dependencies",
    "title_cs": "CorefUD 1.0: Setkání koreference a Universal Dependencies",
    "abstract_en": "Recent advances in standardization for annotated language resources have led to successful large scale efforts, such as the Universal Dependencies (UD) project for multilingual syntactically annotated data. By comparison, the important task of coreference resolution, which clusters multiple mentions of entities in a text, has yet to be standardized in terms of data formats or annotation guidelines. In this paper we present CorefUD, a multilingual collection of corpora and a standardized format for coreference resolution, compatible with morphosyntactic annotations in the UD framework and including facilities for related tasks such as named entity recognition, which forms a first step in the direction of convergence for coreference resolution across languages.",
    "abstract_cs": "Nedávný pokrok ve standardizaci anotovaných jazykových zdrojů vedl k úspěšným velkým projektům jako Universal Dependencies (UD), kde se syntakticky anotují data pro mnoho jazyků. Anotace koreference, která spojuje opakované zmínky téže entity v textu a je pro porozumění jazyku velmi důležitá, je zatím standardizačním úsilím relativně nepoznamenaná. V tomto článku prezentujeme CorefUD, mnohojazyčnou sbírku korpusů a standardizovaný formát pro anotaci koreference, kompatibilní s morfosyntaktickou anotací v UD a rozšiřitelný na příbuzné úlohy, jako je rozpoznávání pojmenovaných entit. Jde o první krok směrem ke konvergenci koreferenčních zdrojů napříč jazyky.", 
    "authors": ["Anna Nedoluzhko", "Michal Novák", "Martin Popel", "Zdeněk Žabokrtský", "Amir Zeldes", "Daniel Zeman"],
    "s2_url": "https://www.semanticscholar.org/paper/33336cdc37455107ca34636d844ab352e410eb1a/"
}
```

<!-- LINDAT description -->
<!-- This is a parallel corpus of Czech and mostly English abstracts of scientific papers and presentations published by authors from the Institute of Formal and Applied Linguistics, Charles University in Prague. For each publication record, the authors are obliged to provide both the original abstract (in Czech or English), and its translation (English or Czech) in the internal Biblio system. The data was filtered for duplicates and missing entries, ensuring that every record is bilingual. Additionally, records of published papers which are indexed by SemanticScholar contain the respective link. The dataset is stored in JSONL format, with each line corresponding to one record. -->