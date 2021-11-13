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

# check there is at least one sequence, and if there more than 1000, only use the first 1000.  

if len(sequences) < 1	:
	print("Error: No sequences detected in " + input_file + ". Exiting pipeline.")
	quit

if len(sequences) > 1000	:
	print("There are too many in this protein family for this subgroup, so using only the first 1000")


# To check conservation, use numpy to create a matrix (Lecture 13, conditionals). Find percent conservation between sequences and make a heatmap. label with species

# I think /localdisk/data/BPSM/Assignment2/pullseq can extract sequneces, so could be used to extract the desired number of sequences

# split into list for species, so get unique species names occuring in the list of lists, make a object for each species, containing all sequences


# as the sequences are large, may use clustalo to align
# plotcon can be used to plot the conservation  

# pd.read_csv() to read as dataframe. Very similar to R! pandas is basically R for python

