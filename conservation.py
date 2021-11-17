#!/urs/local/bin/python3

# import packages 

import sys
import os
import numpy as np
import pandas as pd

input_file = ["input.fasta"]

# script to check and plot (as a heatmap) the conservation between the sequences 
# potentially multiple sequences for each species? so could plot both conservation within a species.

# check: does input file exist with try and except. if file does not exist, exit and return error. 

for file in input_file		:
	try:

		with open(file) as my_file:
     			fasta_data = my_file.read()

	except IOError:

		print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
		quit()

# create a list, each item being a sequence with its header 

sequences = fasta_data.split('>')

# To check conservation, use numpy to create a matrix (Lecture 13, conditionals). Find percent conservation between sequences and make a heatmap. label with species

# check that Amino acids match the amino acid codes. if any dont, then change to X
# regular expressions, find amono acids that are not in the expected letters, change wrong letters to X

# I think /localdisk/data/BPSM/Assignment2/pullseq can extract sequneces, so could be used to extract the desired number of sequences
# split into list for species, so get unique species names occuring in the list of lists, make a object for each species, containing all sequences


# as the sequences are large, may use clustalo to align
# plotcon can be used to plot the conservation
# plotcon -sequences aligned_test.fasta  -graph x11 
# produces a line graph showing the regions with high conservation

# pd.read_csv() to read as dataframe. Very similar to R! pandas is basically R for python


# clustalo -i test.fasta -o aligned_test.fasta -v produces alignment file, can have set max number of sequences and max sequence length

# clustalo --percent-id --full-iter -i test.fasta -o aligned_test.fasta -v --force --clustering-out=cluster.txt. percent id doesnt seem to do anything, cluster.txt is confusing 

