# Usage: python3 encodingSeq_test.py test.data int(flanking size)

import numpy as np
import sys
from six.moves import cPickle as pickle

def encode(c):
    """
    Encoding, ACGT => 1234
    """ 
    if c in ['A', 'a']:
        return 0
    elif c in ['C', 'c']:
        return 1
    elif c in ['G', 'g']:
        return 2
    elif c in ['T', 't']:
        return 3
    else:
        sys.exit()

def encodingSeq2PWM(test_data, f):
    test_file = test_data
    if isinstance(test_file, str):
        test_file_f = open(test_file, 'r')

    #data structure (sample_size, 101*2f, 4)
    data  = np.zeros((1, 101 + 2*f ,4), dtype=np.float32)
    #build flanking block
    flanking = np.array([0.25 for i in range(f*4)]).reshape(f, 4)
    i = 0
    for line in test_file_f:
        i = i+1
        if i % 1000 == 0:
            print(i, '/ 19383')
        seq = line.split('\n')[0]
        #store data
        idx = np.asarray(list(map(encode, seq)))
        c = (np.arange(4) == idx[:, np.newaxis]).astype(np.float32)
        e = np.insert(c ,0, flanking, axis=0)
        e = np.insert(e ,e.shape[0] , flanking, axis=0)
        e = e[np.newaxis, :]
        data = np.concatenate((data, e))

    #delete first sample. (fake one)
    data = np.delete(data, 0, 0)
    #save as a pickle file
    pack = {'seq':data}
    file_name = 'test_f' + str(f) + '.pickle'
    fh = open(file_name, 'wb')
    pickle.dump(pack,fh)
    fh.close()

    #read from pickle file
    fh = open(file_name, 'rb')
    save = pickle.load(fh)
    seq = save['seq']

    test_file_f.close()

if  __name__ == '__main__':

    import sys
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="")
    parser.add_argument('test_data', type=str, help='')
    parser.add_argument('flanking_len', type=int, help='')

    args = parser.parse_args()
    
    encodingSeq2PWM(args.test_data, args.flanking_len)
