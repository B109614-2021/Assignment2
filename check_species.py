#!/usr/local/bin/python3

# get protein family for query sequence
# get organism
# get all sequences and save into a file

import os
import re
import sys
import subprocess
import pandas
import shutil

input_file_name = 'aves_glucose-6-phosphatase.fasta'

all_species = []
all_seq_ids = []


with open(input_file_name , 'r') as my_file:
                file_data = my_file.read()

# split into lines
sequence_data = file_data.split("\n")

# read the whole file line by line
for line in sequence_data:
#	print(line)
        # extract the bit in brackets, corresponding to the species
	species = re.findall('\[.*\]', line)
#	print(species)
	all_species.extend(species)
	id = re.findall('>\S*', line)
#	print(id)
	all_seq_ids.extend(id)


# loop over all species/ids based on the length on the id file. they should be the same length
# remove the brackets and the >
# save into a csv file

	
# print(all_species)
# print(set(all_species))
# print(all_seq_ids)

# save this in a file with counts 
