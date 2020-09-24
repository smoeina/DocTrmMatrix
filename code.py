"""
--  *******************************************************
--  Information Retrieval Course
--  Amirkabir University of Technology (Tehran Polytechnic)
--  Department of Computer Engineering (CE-AUT)
--  https://ce[dot]aut[dot]ac[dot]ir
--  Developed by Seyed Moein Ayyoubzadeh
--  *******************************************************
--  All Rights reserved (C) 2019-2020
--  *******************************************************
--  Additional Comments:

-----------------------------------------------------------
"""

import glob
import os
import numpy as np
import pandas as pd
words = set()

for filename in glob.glob('*.txt'):
    with open(os.path.join(filename), 'r',encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            words_in_line = line.split()
            for word in words_in_line:
                words.add(word)

print(words)
matrix = list()
filenames = list()
for filename in glob.glob('*.txt'):
    filenames.append(filename)
    words_in_this_file = set()
    with open(os.path.join(filename), 'r',encoding="utf8") as f:
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
print(matrix.shape)

matrix = matrix.transpose()

print(matrix)

dataframe = pd.DataFrame(matrix,index=words,columns=filenames)
print(dataframe)

query = input("Enter Your Query: ").split("AND")
print(query)