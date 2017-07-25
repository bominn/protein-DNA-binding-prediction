protein-DNA-binding-prediction
===

## Data description
source: CHIP-seq data https://www.encodeproject.org/experiments/ENCSR000AQU/

> **Training data**  <br/>
> size = 77531 <br/>
> data format example (abbrev.): >chr3:13238050-13238150 CTGGCTGTCA...AGAAGAACAC 1

> **Testing data** <br/>
> size = 19383 <br/>
> data format example (abbrev.): CAGTTGGCCT...CACAAGTAGA

> **Testing data with label** <br/>
> size = 19383 <br/>
> data format example (abbrev.): >chr20:42901189-42901289 CAGTTGGCCT...CACAAGTAGA 1

|        | chromosome number | loci | sequence | label |
|:--:|:--:|:--:|:--:|:--:|
| train.data | chr # | loci | length = 101 | 0 negative, 1 positive |
| test.data | N/A| N/A | length = 101 | N/A |
| test_ans.data | chr # | loci | length = 101 | 0 negative, 1 positive |


