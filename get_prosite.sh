#!/bin/bash

import string
import sys
import os
import numpy as np
import pandas as pd

# run acommand via commandline to run a sequnece through PROSITE ie get  https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?seq=P98073
# can use sequence name to run it, which may be in the fasta file 
# use command GET, with the url attached to it.

### make directory to hold output

os.mkdir('temp/motifs')

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

# patmatmotifs currently only takes first sequence in the fasta file
# for each element, want to save it in a file, perform patmatmotifs analysis
# copy output file output into a growing file which will contain patmatmotifs results for all sequences 

for sequence in sequence_data_list	:
	# read the ">" so fasta file works
	sequence.replace(">", "")
	sequence = ">" + sequence

	# save sequence in a temp file, this will be overwritten with each iteration
	temp_patmat_input = open("temp_patmat__sequences.fasta", "w")
	temp_patmat_input.write(sequence)
	temp_patmat_input.close()

	# run patmatmotifs on temporary file 
	os.system("patmatmotifs -sequence temp_patmat__sequences.fasta -rdirectory2 temp/motifs -auto")

### check that values are expected for amino acids 


### for each sequence header, provide a list of motifs identified for each sequence

# use patmatmotifs
# currently only takes first sequence in the fasta file 

### make a barplot of some sort 


# then grep for motifs, count up number of motifs and produce both a file showing what motifs occur on each sequence, and a bar plot of the most common.

# use os.system to run bash commandline commands
