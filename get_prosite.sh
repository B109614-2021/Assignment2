#!/bin/bash

import string
import sys
import os
import numpy as np
import pandas as pd

# run acommand via commandline to run a sequnece through PROSITE ie get  https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?seq=P98073
# can use sequence name to run it, which may be in the fasta file 
# use command GET, with the url attached to it.

### open file, give them the choice of partical, Predicted, complete or all

input_file = "temp/aves_glucose-6-phosphatase.fasta"

try:
        with open(input_file) as my_file:
                sequence_data = my_file.read()

except IOError:

        print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
        quit()


### extract sequences

# split each fasta element into its own part of a list
sequence_data_list = sequence_data.split(">")

# print(sequence_data_list)

# make a new file
# for each element in the list
#	split at ']\n'
# 	paste the first element into the file
#	call prosite, using the second element as the input sequence
# 	save the the output into the file  


### check that values are expected for amino acids 


### for each sequence header, provide a list of motifs identified for each sequence

# use patmatmotifs

### make a barplot of some sort 


# then grep for motifs, count up number of motifs and produce both a file showing what motifs occur on each sequence, and a bar plot of the most common.

# use os.system to run bash commandline commands
