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

# To check conservation, use numpy to create a matrix (Lecture 13, conditionals). Find percent conservation between sequences and make a heatmap. label with species

# check that Amino acids match the amino acid codes. if any dont, then change to X
# regular expressions, find amono acids that are not in the expected letters, change wrong letters to X
# resave to new file, which is then used for clustalo for alignment and then checking which regions are conserved.


# as the sequences are large, may use clustalo to align
# plotcon can be used to plot the conservation
# plotcon -sequences aligned_test.fasta -graph svg probably best.  
# produces a line graph showing the regions with high conservation

# need to put in python script os.systemcall()

# clustalo -i test.fasta -o aligned_test.fasta -v produces alignment file, can have set max number of sequences and max sequence length

# clustalo --percent-id --full-iter -i test.fasta -o aligned_test.fasta -v --force --clustering-out=cluster.txt. percent id doesnt seem to do anything, cluster.txt is confusing 

# plotcon -sequences aligned_test.fasta -graph svg -winsize (find best window size) 
# add graph variables to make pretty 
# "-graph" associated qualifiers
#   -gprompt            boolean    Graph prompting
#   -gdesc              string     Graph description
#   -gtitle             string     Graph title
#   -gsubtitle          string     Graph subtitle
#   -gxtitle            string     Graph x axis title
#   -gytitle            string     Graph y axis title
#   -goutfile           string     Output file for non interactive displays
#   -gdirectory         string     Output directory

