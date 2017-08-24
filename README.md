protein-DNA-binding-prediction
===
## Usage of python program
```
python3 encodingSeq_train.py train.data 10(flanking length)
python3 encodingSeq_test.py test.data 10(flanking length)
```
## Task description
The objective of this task is to correctly predict whether CTCF protein can bind on the given DNA sequence, and I tried to finish the task by using the CNN technique of deep learning. The approach mentioned below was inspired by MNIST hand-written digit classification.


## Data description
* Data source: CHIP-seq data from https://www.encodeproject.org/experiments/ENCSR000AQU/
* Each column is separated by 'one space'.

* **Training data**  <br/>
> sample size: 77531 <br/>
> data format example (abbrev.): >chr3:13238050-13238150 CTGGCTGTCA...AGAAGAACAC 1

* **Testing data** <br/>
> samlpe size: 19383 <br/>
> data format example (abbrev.): CAGTTGGCCT...CACAAGTAGA

* **Testing data with label** <br/>
> sample size: 19383 (9709 positive, 9674 negative) <br/>
> data format example (abbrev.): >chr20:42901189-42901289 CAGTTGGCCT...CACAAGTAGA 1

| file name | chromosome number | loci | sequence length | label |
| :--: | :--: | :--: | :--: | :--: |
| train.data | chr # | loci | 101 | 0 negative, 1 positive |
| test.data | N / A| N / A | 101 | N / A |
| test_ans.data.txt | chr # | loci | 101 | 0 negative, 1 positive |

## Preprocessing
I use encodingSeq_train.py and encodingSeq_test.py to convert train.data and test.data to pickle format, turning the sequence data into one-hot encoding form. Besides, the flanking length of the sequence can be determined by users.

## Model description
```
def model_train(data):
    conv = tf.nn.conv2d(data, layer1_weights, [1, stride_1, stride_1, 1], padding='SAME')
    hidden = tf.nn.relu(conv + layer1_biases)
    drop = tf.nn.dropout(hidden, 0.75)
    conv = tf.nn.conv2d(drop, layer2_weights, [1, stride_2, stride_2, 1], padding='SAME')
    hidden = tf.nn.relu(conv + layer2_biases)
    drop = tf.nn.dropout(hidden, 0.75)
    shape = hidden.get_shape().as_list()
    reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
    hidden = tf.nn.relu(tf.matmul(reshape, layer3_weights) + layer3_biases)
    drop = tf.nn.dropout(hidden, 0.75)
    hidden = tf.nn.relu(tf.matmul(drop, layer4_weights) + layer4_biases)
    return tf.matmul(hidden, layer5_weights) + layer5_biases
```
```
def model(data):
    conv = tf.nn.conv2d(data, layer1_weights, [1, stride_1, stride_1, 1], padding='SAME')
    hidden = tf.nn.relu(conv + layer1_biases)
    conv = tf.nn.conv2d(drop, layer2_weights, [1, stride_2, stride_2, 1], padding='SAME')
    hidden = tf.nn.relu(conv + layer2_biases)
    shape = hidden.get_shape().as_list()
    reshape = tf.reshape(hidden, [shape[0], shape[1] * shape[2] * shape[3]])
    hidden = tf.nn.relu(tf.matmul(reshape, layer3_weights) + layer3_biases)
    hidden = tf.nn.relu(tf.matmul(drop, layer4_weights) + layer4_biases)
    return tf.matmul(hidden, layer5_weights) + layer5_biases
```
## Training parameters and settings
* batch size = 290 (train_dataset.shape[0] // 200) <br/>
* training steps = 15000 <br/>
* learning rate = 0.25 (starting rate) with exponential decay after 5000 steps, decay rate = 0.96 <br/>
* optimizer: GradientDescentOptimize <br/>
* using regularization to eliminate overfitting circumstances

## Results
* Training process

| Steps | minibatch loss | minibatch accuracy | validation accuracy |
| :--: | :--: | :--: | :--: |
| 0 | 1.036431 | 52.759 % | 50.663 %	|
| 500 | 0.683988 | 62.069 % | 60.486 % |
| 1000 | 0.624465 | 65.862 % | 71.129 % |
| 1500 | 0.633703 | 68.276 % | 78.105 % |
| 2000 | 0.470493 | 78.621 % | 84.543 % |
| 2500 | 0.467052 | 81.724 % | 80.426 % |
| 3000 | 0.340815 | 85.517 % | 87.535 % |
| 3500 | 0.343168 | 87.241 % | 88.155 % |
| 4000 | 0.281665 | 90.000 % | 88.222 % |
| 4500 | 0.316459 | 89.310 % | 89.223 % |
| 5000 | 0.306602 | 88.621 % | 89.651 % |
| 5500 | 0.323350 | 85.517 % | 89.656 % |
| 6000 | 0.370277 | 84.828 % | 88.278 % |
| 6500 | 0.326758 | 86.897 % | 89.764 % |
| 7000 | 0.319943 | 87.586 % | 90.069 % |
| 7500 | 0.260177 | 90.345 % | 90.058 % |
| 8000 | 0.330911 | 87.931 % | 89.795 % |
| 8500 | 0.266430 | 91.034 % | 90.378 % |
| 9000 | 0.265763 | 90.000 % | 90.528 % |
| 9500 | 0.285275 | 91.724 % | 90.358 % |
| 10000 | 0.260739 | 90.690 % | 90.487 % |
| 10500 | 0.273746 | 89.655 % | 89.919 % |
| 11000 | 0.281265 | 91.034 % | 90.590 % |
| 11500 | 0.278727 | 91.034 % | 90.512 % |
| 12000 | 0.310407 | 88.621 % | 90.595 % |
| 12500 | 0.282559 | 87.586 % | 90.523 % |
| 13000 | 0.295398 | 89.310 % | 90.812 % |
| 13500 | 0.254486 | 90.000 % | 90.636 % |
| 14000 | 0.266505 | 89.655 % | 90.672 % |
| 14500 | 0.257149 | 90.690 % | 90.579 % |
| 15000 | 0.259550 | 88.966 % | 90.559 % |

<img src="https://github.com/andrewkgs/protein-DNA-binding-prediction/blob/master/training_accuracy.png"> <br/>
* **Test accuracy: 90.517 %**


## Future work
The model I used in the task is not complicated at all, and maybe trying models with more layers can get better results.
Also, I think RNN is an another way to build or improve the model.

## Reference
> MNIST CNN tutorial <br/>
> https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/udacity

> DeepBind <br/>
> http://www.nature.com/nbt/journal/v33/n8/full/nbt.3300.html <br/>
> http://www.nature.com/nbt/journal/v33/n8/extref/nbt.3300-S2.pdf
