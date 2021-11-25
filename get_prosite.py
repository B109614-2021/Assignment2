#!/usr/local/bin/python3

import string
import sys
import os
import re
import csv

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

### get motif counts 

# use re.search('.* Motif = .', ) to find the motifs 

patmat_output_files = os.listdir('temp/motifs')

# print(patmat_output_files)

# create an empty list to hold motifs 

total_motifs = []

for file in patmat_output_files:

	# recreate the whole file path
	file_path = 'temp/motifs/' + file

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

# print(total_motifs)
# print(set(total_motifs))

# want to make a csv file with motifs identifies and their numbers 

with open('motif_summary.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile)
	filewriter.writerow(['Motif', 'Number of hits'])

	# add a new row for each motif and trim 'Motif = ' from the front

	for motif in set(total_motifs):
		motif_trim = motif.replace("Motif = ", "")
		filewriter.writerow([motif_trim, total_motifs.count(motif)])


### make a summary file/plot

# potentiall make a bar chart plotting the different motifs and their occurances 
