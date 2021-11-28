#!/usr/local/bin/python3

import string
import sys
import subprocess
import os
import re
import csv

# This script identifies motifs in the desired type sequence 

### open file, give them the choice of partial, Predicted, complete or all

# make a directory in temp to hold all the outputs of patmatmotifs
os.mkdir('temp/motifs')

input_file = "temp/" + sequence_type + "_sequences.fasta"

try:
        with open(input_file) as my_file:
                sequence_data = my_file.read()

except IOError:

        print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
        quit()

print('Finding motifs using patmatmotifs')

### extract sequences

# split each fasta element into its own part of a list

sequence_data_list = sequence_data.split(">")

# print(sequence_data_list)

# patmatmotifs currently only takes first sequence in the fasta file
# for each element, want to save it in a file, perform patmatmotifs analysis
# copy output file output into a growing file which will contain patmatmotifs results for all sequences 

# as there is > at the start, the list will have empty values, need to remove these

while("" in sequence_data_list) :
    sequence_data_list.remove("")

for sequence in sequence_data_list	:
	# read the ">" so fasta file works
	sequence.replace(">", "")
	sequence = ">" + sequence

	# save sequence in a temp file, this will be overwritten with each iteration
	temp_patmat_input = open("temp/temp_patmat__sequences.fasta", "w")
	temp_patmat_input.write(sequence)
	temp_patmat_input.close()

	# run patmatmotifs on temporary file, some may have 0 lengths if there were any blamk lines so catch errors and warnings
	try:
		os.system("patmatmotifs -sequence temp/temp_patmat__sequences.fasta -rdirectory2 temp/motifs -auto")
	except:
		pass

### get motif counts 

# use re.search('.* Motif = .', ) to find the motifs 

patmat_output_files = os.listdir('temp/motifs')

# print(patmat_output_files)

# create an empty list to hold motifs 

total_motifs = []
id_motifs = {}

for file in patmat_output_files:

	# print(file)
	# recreate the whole file path
	file_path = 'temp/motifs/' + file
	file_id = file.replace('.patmatmotifs','')

	with open(file_path, 'r') as my_file:
		motif_data = my_file.read()

	# split into lines 
	motif_data = motif_data.split("\n")
	 
	# read the whole file line by line
	for line in motif_data:
#		print(line)
		motif = re.findall('.*Motif = .*', line)
#		print(motif) 
		total_motifs.extend(motif)
		
		if file_id in id_motifs:
					
			# make a dict, if the key already exists add to value
			id_motifs[file_id] = id_motifs[file_id] + motif

		else:

			id_motifs[file_id] = motif
	
# print(id_motifs)

# create a file listing the IDs and Motifs, currently has 'Motif =' before each detected motif 

print('Creating summary files of identified motifs and sequences')

with open('output/id_motif.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile)
	filewriter.writerow(['Id', 'Motifs']) 
	
	# add the IDs and motifs to file
	for ID in id_motifs.keys():
		filewriter.writerow([ID, id_motifs[ID]])

# next step, remove "Motif = " from each element

# print(total_motifs)
# print(set(total_motifs))

# want to make a csv file with motifs identifies and their numbers 

with open('output/motif_summary.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile)
	filewriter.writerow(['Motif', 'Number of hits'])

	# add a new row for each motif and trim 'Motif = ' from the front

	for motif in set(total_motifs):
		motif_trim = motif.replace("Motif = ", "")
		filewriter.writerow([motif_trim, total_motifs.count(motif)])


### zip the motif files

shutil.make_archive("temp/motifs", "zip", "temp/motifs")

### remove non zipped files

try:
        shutil.rmtree('temp/motifs')
except OSError as e:
        # it is likely that temp does not exist, so don't want error to break the pipeline
        print("Error: %s : %s" % ('temp', e.strerror))

# remove temporary file
os.remove('temp/temp_patmat__sequences.fasta')

