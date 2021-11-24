#!/urs/local/bin/python3

# import packages 

import string
import sys
import os
import numpy as np
import pandas as pd

input_file = "temp/aves_glucose-6-phosphatase.fasta"

# print(input_file)
# check: does input file exist with try and except. if file does not exist, exit and return error. 

try:
	with open(input_file) as my_file:
     		fasta_data = my_file.read()

except IOError:

	print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
	quit()

# check that Amino acids match the amino acid codes. if any dont, then change to X
# regular expressions, find amono acids that are not in the expected letters, change wrong letters to X
# resave to new file, which is then used for clustalo for alignment and then checking which regions are conserved.

# print(fasta_data)

# print(type(fasta_data))
# fasta_data is a string, split into a list where > occurs using .split, so each header and sequence is a different object

fasta_data_list = fasta_data.split(">")

# print(fasta_data_list)
# need to re add ">" to the start of sequences 


### split into partial, predicted and full sequences

# create new fasta files

my_outfile_partial = open("partial_sequences.fasta", "w")
my_outfile_predicted = open("predicted_sequences.fasta", "w")
my_outfile_complete = open("complete_sequences.fasta", "w")

for sequence in fasta_data_list	:
	sequence.replace(">", "")
	sequence = ">" + sequence
	# print(sequence) 
	if("partial" in sequence):
	# 	print("is a partial sequence")
		my_outfile_partial.write(sequence)
	elif("PREDICTED" in sequence):
	# 	print("is a predicted sequence")
		my_outfile_predicted.write(sequence)

	else:
	#	print("is a complete sequnece")
		my_outfile_complete.write(sequence)

my_outfile_partial.close()
my_outfile_predicted.close()
my_outfile_complete.close()

### desired file (likely complete) can be used for clustalo

# use clustalo to align
# plotcon can be used to plot the conservation
# plotcon -sequences aligned_test.fasta -graph svg probably best.  
# produces a line graph showing the regions with high conservation

### need to put in python script os.systemcall()
### need to make general
### need to let user pick whether they want to use complete, partial or predicted
### need to check for species number and ask user if they want to check within or between species (why not both!)
### need to pass variables from one script to another

# clustalo -i test.fasta -o aligned_test.fasta -v produces alignment file, can have set max number of sequences and max sequence length

# clustalo --percent-id --full-iter -i test.fasta -o aligned_test.fasta -v --force --clustering-out=cluster.txt. percent id doesnt seem to do anything, cluster.txt is confusing 

# plotcon -sequences aligned_test.fasta -winsize 10 -graph svg. winsize 10 makes nicer looking graph than smaller numbers, but still contains information  

# need to return to screen as well as an svg
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

