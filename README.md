# ÚFAL Bilingual Abstracts Corpus

This is a parallel corpus of Czech and mostly English abstracts of scientific papers and presentations published by authors from the [Institute of Formal and Applied Linguistics](https://ufal.mff.cuni.cz/), Charles University in Prague.
For each publication record, the authors are obliged to provide both the original abstract (in Czech or English), and its translation (English or Czech) in the internal Biblio system.
The data was filtered for duplicates and missing entries, ensuring that every record is bilingual.
Additionally, records of published papers which are indexed by SemanticScholar contain the respective link.
The dataset was created from September 2022 image of the Biblio database and is stored in JSONL format, with each line corresponding to one record.

You can download the dataset [here on Lindat](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-4922) or directly from the command-line:

```
wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-4922/corpus.jsonl
```

## Reproducing the dataset

To replicate the results, simply put `authors.xml` and `publications.xml` (from the Biblio system) to `data/` and run the `main.py` script.
If you are also interested in links to SemanticScholar, you may get them by running `main.py -s2` (expect much slower runtime).

You can run `statistics.py` to get an overview for the dataset:

|||
|-|-|
|Total records                      | 2659  |
|Average sents (words) per abstract | 4.0 (96.0)  |
|Total sents (words) (en)           | 11k (255k)  |
|Langs                              | en 2086 (78.5%), cs 548 (20.6%), ru 13 (0.5%), ... (long tail of less-represented languages)  |
|Papers with S2 links               | 47.2%  |
|Publication year                   | 2022: 65, 2021: 204, 2020: 161, 2019: 147, 2018: 173, 2017: 183, 2016: 205, 2015: 169, 2014: 187, 2013: 155, 2012: 146, 2011: 123, 2010: 146, 2009: 132, 2008: 133, 2007: 105, 2006:  113, 2005: 79, 2004: 13, 2003: 4, 2002: 5, 2001: 3, 2000: 4, 1998: 3, 1997: 1 |

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

## Citation

The corpus was created by [Rudolf Rosa](mailto:rosa@ufal.mff.cuni.cz) and [Vilém Zouhar](mailto:vzouhar@inf.ethz.ch).
Contact the authors if you are experiencing any difficulties while using this dataset or have any related questions. 
For citation, please use the following BibTeX entry:

```
@misc{11234/1-4922,
    title = {Czech and English abstracts of {{\'U}FAL} papers (2022-11-11)},
    author = {Rosa, Rudolf and Zouhar, Vil{\'e}m},
    url = {http://hdl.handle.net/11234/1-4922},
    note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
    copyright = {Creative Commons - Attribution 4.0 International ({CC} {BY} 4.0)},
    year = {2022}
}
```
