protein-DNA-binding-prediction
===
## Usage of python program
```
python3 encodingSeq_train.py train.data 10(flanking length)
python3 encodingSeq_test.py test.data 10(flanking length)
```
## Task description
The objective of this task is to correctly predict whether the given DNA sequence can bind on CTCF protein, and I tried to finish the task by using the CNN technique of deep learning.


## Data description
* Data source: CHIP-seq data https://www.encodeproject.org/experiments/ENCSR000AQU/
* Each column is separated by 'one space'.

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
| test.data | N / A| N / A | length = 101 | N / A |
| test_ans.data.txt | chr # | loci | length = 101 | 0 negative, 1 positive |

## Preprocessing
I use encodingSeq_train.py and encodingSeq_test.py to convert train.data and test.data to pickle format, turning the sequence data into one-hot encoding form. Besides, the flanking length of the sequence can be determined by users.

## Model description
```
conv = tf.nn.conv2d(data, layer1_weights, [1, stride_1, stride_1, 1], padding='SAME')
hidden = tf.nn.relu(conv + layer1_biases)
conv = tf.nn.conv2d(hidden, layer2_weights, [1, stride_2, stride_2, 1], padding='SAME')
hidden = tf.nn.relu(conv + layer2_biases)
shape = hidden.get_shape().as_list()
reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
hidden = tf.nn.relu(tf.matmul(reshape, layer3_weights) + layer3_biases)
drop = tf.nn.dropout(hidden, 0.7)
hidden = tf.nn.relu(tf.matmul(drop, layer4_weights) + layer4_biases)
drop = tf.nn.dropout(hidden, 0.7)
return tf.matmul(drop, layer5_weights) + layer5_biases
```

## Training parameters and settings
> batch size = 256 <br/>
> training steps = 10000 <br/>
> learning rate = 0.25 (starting rate) with exponential decay after 6000 steps, decay rate = 0.88 <br/>
> optimizer: GradientDescentOptimize <br/>
> using regularization to eliminate overfitting circumstances

## Results
* Training process

| Steps | minibatch loss | minibatch accuracy | validation accuracy |
| :--: | :--: | :--: | :--: |
| 0 | 1.573298 | 47.266 %	| 49.337 % |
| 500	| 0.789611	| 57.031 % | 60.610 % |
| 1000 | 0.618249	| 74.609 %	| 72.858 % |
| 1500 | 0.538275	| 78.516 %	| 77.651 % |
| 2000 | 0.525321	| 82.422 % | 82.216 % |
| 2500 | 0.452186	| 82.812 %	| 83.434 % |
| 3000 | 0.373034	| 87.109 %	| 87.056 % |
| 3500 | 0.355203	| 89.844 %	| 87.546 % |
| 4000 | 0.355099	| 89.844 %	| 87.437 % |
| 4500 | 0.410359	| 86.719 %	| 87.484 % |
| 5000 | 0.281168	| 91.016 %	| 89.212 % |
| 5500 | 0.282837	| 91.406 %	| 89.274 % |
| 6000 | 0.357626	| 86.719 %	| 86.416 % |
| 6500 | 0.244438 | 93.359 %	| 89.677 % |
| 7000 | 0.261607 | 90.234 %	| 86.973 % |
| 7500 | 0.188995	| 94.922 %	| 89.883 % |
| 8000 | 0.231573	| 91.016 %	| 89.548 % |
| 8500 | 0.181226	| 94.531 %	| 89.130 % |
| 9000 | 0.251837	| 92.188 %	| 89.677 % |
| 9500 | 0.245221	| 91.406 %	| 88.268 % |
| 10000 | 0.247332	| 91.797 %	| 89.026 % |

<img src="https://github.com/andrewkgs/protein-DNA-binding-prediction/blob/master/result.png"> <br/>
* **Test accuracy = 89.006 %**


## Future work
The model I used in the task is not complicated at all, and maybe trying models with more layers can get better results.
ALso, I think RNN is an another way to build the model.

## Reference
> MNIST CNN tutorial <br/>
> https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/udacity

> DeepBind <br/>
> http://www.nature.com/nbt/journal/v33/n8/full/nbt.3300.html <br/>
> http://www.nature.com/nbt/journal/v33/n8/extref/nbt.3300-S2.pdf
