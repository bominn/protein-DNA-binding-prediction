protein-DNA-binding-prediction
===

## Data description
source: CHIP-seq data https://www.encodeproject.org/experiments/ENCSR000AQU/
* each column is separted by 'one space'

> **Training data**  <br/>
> sample size = 77531 <br/>
> data format example (abbrev.): >chr3:13238050-13238150 CTGGCTGTCA...AGAAGAACAC 1

> **Testing data** <br/>
> samlpe size = 19383 <br/>
> data format example (abbrev.): CAGTTGGCCT...CACAAGTAGA

> **Testing data with label** <br/>
> sample size = 19383 (9709 positive, 9674 negative) <br/>
> data format example (abbrev.): >chr20:42901189-42901289 CAGTTGGCCT...CACAAGTAGA 1

| file name | chromosome number | loci | sequence | label |
| :--: | :--: | :--: | :--: | :--: |
| train.data | chr # | loci | length = 101 | 0 negative, 1 positive |
| test.data | N/A| N/A | length = 101 | N/A |
| test_ans.data.txt | chr # | loci | length = 101 | 0 negative, 1 positive |

## Preprocessing


## Model description


## Results


## Reference
> MNIST CNN tutorial <br/>
> https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/udacity

> DeepBind <br/>
> http://www.nature.com/nbt/journal/v33/n8/full/nbt.3300.html <br/>
> http://www.nature.com/nbt/journal/v33/n8/extref/nbt.3300-S2.pdf
