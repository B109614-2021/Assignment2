#!/usr/local/bin/python3

import string
import sys
import subprocess
import os
import shutil
import re
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

# pepwindow makes a hydropathy plot for an individual sequence, not particularly helpful as I will potentialy have lots of sequences
# pepinfo checks for different peptide properties at each position. Could use to make my own hydropathy plot 

### make directory to hold pepinfo outputs 

os.mkdir('temp/pepinfo')
os.mkdir('temp/pepinfo/graphs')

### get input file

sequence_type = 'complete'

input_file = "temp/" + sequence_type + "_aligned.fasta"
#  "temp/" + sequence_type + "_sequences.fasta"

try:
        with open(input_file) as my_file:
                sequence_data = my_file.read()

except IOError:

        print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
        quit()


### split into individual sequences and run pepinfo

# as this file has > at the start there will be an empty object created at the start, causing errors 

sequence_data_list = sequence_data.split(">")

while("" in sequence_data_list) :
    sequence_data_list.remove("")

# print(sequence_data_list)

print("Running pepinfo on sequences")

# get the length of the sequence, will use later for a dataframe
max_seq_length = 0

for sequence in sequence_data_list      :
	# read the ">" so fasta file works
	sequence.replace(">", "")
	sequence = ">" + sequence

	# get the id	
	id = re.findall(r'>\S*', sequence)
	id = id[0]
	id = id.replace(">", "")
	# print(id)
	
	# get the length of the sequence, looking for the max data
	protein_sequence = sequence.split("]\n")
	protein_sequence = protein_sequence[1]
	if len(protein_sequence) > max_seq_length:
		max_seq_length = len(protein_sequence)	

	# save sequence in a temp file, this will be overwritten with each iteration
	temp_patmat_input = open("temp/temp_patmat__sequences.fasta", "w")
	temp_patmat_input.write(sequence)
	temp_patmat_input.close()
	
	pepinfo_command = "pepinfo -sequence temp/temp_patmat__sequences.fasta -odirectory2 temp/pepinfo -graph svg -goutfile " + id + " -gdirectory temp/pepinfo/graphs -auto"
	
	# run patmatmotifs on temporary file, some may have 0 lengths if there were any blamk lines so catch errors and warnings
	try:
		os.system(pepinfo_command)
	except:
		pass

### use the pepinfo to calculate the number of polar and nonpolar sequences at each position 

# read in file 
# just want to focus on polar and non polar so extract dataframes with these

patmat_output_files = os.listdir('temp/pepinfo/')

# make a dataframe, want positon, n polar, n non-polar
# make full of 0s and add to later

print("Counting occurances of polar and non polar bases at each position and plotting")

headers = ["position", "polar", "non-polar"]
polarity = pd.DataFrame(0,index=np.arange(max_seq_length), columns=headers)
polarity["position"] = np.arange(max_seq_length)

# print(polarity)

for file in patmat_output_files:
	if '.pepinfo' not in file:
		continue	
	file = "temp/pepinfo/" + file
	# print(file)
	try:
		with open(file) as my_file:
			patmat_info = my_file.read()

	except IOError:
		print('Error: ' + file + ' does not exist.' + ' Exiting pipeline.')
		continue

	# split where there are 4 X \n, which splits the dataframe in the .pepinfo files 
	patmat_info_list = patmat_info.split("\n\n\n\n")
	
	# if the list has no entries, so if the file was somehow empty, go to the next itteration of the loop 
	if len(patmat_info_list) == 0:
		continue
	# print(patmat_info_list)
	for dataframe in patmat_info_list:
		if " Polar " in dataframe:
			polar = dataframe
		if "Non-polar" in dataframe:
			non_polar = dataframe
	# print(polar)
	# print(non_polar)
	
	polar_positions = polar.split("\n")
	non_polar_positions = non_polar.split("\n")	
	
	# remove the wordy bits
	del polar_positions[0:3]
	del non_polar_positions[0:3]
		
	# print(polar_positions)
	# print(non_polar_positions)

	# now just have a list, with each element having a position, an amino acid and a 1 or 0 for presence or absence of Amino acid type 
	for p_position in polar_positions: 
		
		# remove white spaces
		p_position = re.findall(r'\S*', p_position)
		while("" in p_position) :
			p_position.remove("")

		# check if this position has a polar amino acid
		if int(p_position[2]) == 1:
			polarity.at[int(p_position[0]), 'polar'] = polarity.at[int(p_position[0]), 'polar'] +1
		# print(p_position)

	for np_position in non_polar_positions:

		# remove the white space
		np_position = re.findall(r'\S*', np_position)
		while("" in np_position) :
			np_position.remove("")

		# check if this position has a non-polar amino acid
		if int(np_position[2]) == 1:
			polarity.at[int(np_position[0]), 'non-polar'] = polarity.at[int(np_position[0]), 'non-polar'] +1
		# print(np_position)

# print(polarity)

### make a bar plot showing regions of polar and non polar amino acids. As some sequences will not have amino acids at certain positions, the bars will not be of equal height  

fig, ax = plt.subplots()

ax.bar(polarity['position'], polarity['polar'], label='Polar')
ax.bar(polarity['position'], polarity['non-polar'], label='Non-Polar')

ax.set_ylabel('Counts')
ax.set_title('Metafeature plot of polatiry of bases along a metasequence')
ax.legend()

plt.savefig("output/metafeature_base_polarity.png",transparent=True, bbox_inches = 'tight', pad_inches=0.5)

### zip the pepinfo output files, so they are there but not taking up too much space

shutil.make_archive("temp/pepinfo", "zip", "temp/pepinfo")

### remove unzipped pepinfo

try:
        shutil.rmtree('temp/pepinfo')
except OSError as e:
        # it is likely that temp does not exist, so don't want error to break the pipeline
        print("Error: %s : %s" % ('temp', e.strerror))

