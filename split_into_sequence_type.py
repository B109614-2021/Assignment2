#!/urs/local/bin/python3

# import packages

import string
import sys
import os
import numpy as np
import pandas as pd

# print(input_file_name)
# check: does input file exist with try and except. if file does not exist, exit and return error.

try:
        with open(input_file_name) as my_file:
                fasta_data = my_file.read()

except IOError:

        print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
        quit()

# print(fasta_data)

# print(type(fasta_data))

# fasta_data is a string, split into a list where > occurs using .split, so each header and sequence is a different object

fasta_data_list = fasta_data.split(">")

# print(fasta_data_list)
# need to re add ">" to the start of sequences

### split into partial, predicted and full sequences

print("Creating seperate files for complete, partial and predicted sequences")

# create new fasta files

my_outfile_partial = open("temp/partial_sequences.fasta", "w")
my_outfile_predicted = open("temp/predicted_sequences.fasta", "w")
my_outfile_complete = open("temp/complete_sequences.fasta", "w")

for sequence in fasta_data_list :
	sequence.replace(">", "")
	sequence = ">" + sequence
        # print(sequence)
	if("partial" in sequence):
		# print("is a partial sequence")
		my_outfile_partial.write(sequence)
	elif("PREDICTED" in sequence):
		# print("is a predicted sequence")
		my_outfile_predicted.write(sequence)

	else:
		# print("is a complete sequnece")
		my_outfile_complete.write(sequence)

my_outfile_partial.close()
my_outfile_predicted.close()
my_outfile_complete.close()

