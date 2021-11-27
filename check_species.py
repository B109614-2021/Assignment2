#!/usr/local/bin/python3

# get protein family for query sequence
# get organism
# get all sequences and save into a file

import csv
import os
import re
import sys
import subprocess
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
	# print(line)
        # extract the bit in brackets, corresponding to the species
	species = re.findall('\[.*\]', line)
#	print(species)
	all_species.extend(species)
	id = re.findall('>\S*', line)
#	print(id)
	all_seq_ids.extend(id)

# print out the number of occurances of each species. potentially find a way to order by number of occurances

print("Identified " + str(len(set(all_species))) + " species")

for species_identity in set(all_species):
	species_identity_trim = species_identity.replace("[", "")
	species_identity_trim = species_identity_trim.replace("]", "")
	print("there are " + str(all_species.count(species_identity)) + " occurances of " +  species_identity_trim) 

# save in a file so have id matched with a species. could use later or user could use later 
# loop over all species/ids based on the length on the id file. they should be the same length
# remove the brackets and the >
# save into a csv file

with open('output/seq_id_species.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile)

	# create headers
        filewriter.writerow(['Sequence Id', 'Species'])

        # add a new row for each motif and trim 'Motif = ' from the front

        for index in range(len(all_seq_ids)):
		
		# get id at the expected index. as matching ids and species were put in from the same line
		# in the above loop they should have the same index 
		
		# remove the > at the start of the id
		id_at_index = all_seq_ids[index]
		id_at_index = id_at_index.replace(">", "") 
                
		# remove the brackets
		species_at_index = all_species[index]
		species_at_index = species_at_index.replace("[", "")
		species_at_index = species_at_index.replace("]", "")
		
		# write the trimmed versions into the csv file
                filewriter.writerow([id_at_index, species_at_index])


### ask user if they want to continue with current dataset
