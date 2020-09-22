import collections
import glob
import os
import numpy as np
words = set()

for filename in glob.glob('*.txt'):
    with open(os.path.join(filename), 'r') as f:
        lines = f.readlines()
        for line in lines:
            words_in_line = line.split()
            for word in words_in_line:
                words.add(word)

print(words)
matrix = list()
for filename in glob.glob('*.txt'):
    words_in_this_file = set()
    with open(os.path.join(filename), 'r') as f:
        lines = f.readlines()
        for line in lines:
            words_in_line = line.split()
            for word in words_in_line:
                words_in_this_file.add(word)

        for word in words:
            if word in words_in_this_file:
                matrix.append(1)
            else:
                matrix.append(0)

print(matrix)
print(len(words))
matrix = np.reshape(matrix,(len(glob.glob('*.txt')),len(words)))
print(matrix)

