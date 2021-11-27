#!/usr/local/bin/python3

### options:
# calculate GC% 
# plot and compare amino acid sequence/features. even if the underlying sequence is the same are the regions of hydrophobicity etc the same? Pepinfo or Pepwindow
# make some sort of plot comaring regions and their charge, which is most common in each region?

# pepwindow makes a hydropathy plot 
# pepinfo checks for different peptide properties at each position. Could use to make my own hydropathy plot 

# get numpy to make a matrix 

import numpy as np
import os
import re
import sys
import subprocess
import shutil


aligned_input_file = 'aligned_test.fasta'

with open(aligned_input_file , 'r') as my_file:
                aligned_sequence_data = my_file.read()

### get sequences 

# need to split aligned_test.fasta into a list of sequences, removing the header
# split at <, readd <, remove lines starting with <?

sequence_data = aligned_sequence_data.split('>')

# create a dict to hold ids and sequences

id_sequence = {}

for sequence in sequence_data:
	# print(sequence)
	sequence = '>' + sequence
	# extract the id and sequence for enteries that are longer then 1 (blank lines will become >, so have a length of 1)
	if len(sequence) > 1:
		# use the > to find the sequence is
		id = re.findall(r'>\S*', sequence)
		# print(id)
		
		# find all returns a list, take the first element, which will be the id, and remove the >
		id = id[0].replace(">","")

		# split into header and sequence, include ] to specify split at header
		protein_sequence = sequence.split("]\n")
		print(protein_sequence[1])
		
		# save into a dict, with ID as the key 
		id_sequence[id] = protein_sequence[1]

print(id_sequence)

# make a dict of ids and sequences 

### build empty similarity matrix, should have the same length as there are sequences 

# want a matrix labelled with IDs on the axi


### function to calculate similarity score	

def cal_seq_sim(seq_of_interest, comparison):
	
	# paste seq and comparison seq together
	myseqs = seq_of_interest + comparison
	#print(myseqs)
	
	# make empty matrix to calculate identity
	IDmatrix = np.eye(len(myseqs),dtype=int)
	
	# make a counter for the sequence matrix 
	xcounter=0
	
	# create a matrix comparing the similarity between each base 
	for xbase in myseqs :
		xcounter+=1
		ycounter=0
		for ybase in myseqs :
			ycounter+=1
			# print(xcounter,ycounter,xbase,ybase)
			if ybase==xbase :
				IDmatrix[(xcounter-1),(ycounter-1)]=1

	# as using the aligned version, the sequences should have the same length. therefor take the diagonal from the halfway point
	return(int(IDmatrix[0:int(len(myseqs)/2),int(len(myseqs)/2):len(myseqs)].diagonal().sum()/int(len(myseqs)/2)*100))

	# print(IDmatrix[0:len(myseqs),0:len(myseqs)])
	# print("The similarity was",int((IDmatrix[0:int(len(myseqs)/2),int(len(myseqs)/2):len(myseqs)].diagonal().sum()/9)*100),"percent")

# take this similarity value and add to a matrix, for position seq, comparison seq

# test that the function works the same as the one in the lecture, returns 66 as expected
# similarity = cal_seq_sim('ATTGTACGG','AATGAACCG')
# print(similarity)

### get similarity values 


### make a dendrogram out of sequence similarity. could label with id, and then use ID_species.csv to colour by species. 

# are sequences from the same species clustered? 


# for each sequence, get its similarity score to other sequences in the group, add a row of percent similarity to sequences to a growing matrix
# use these similarity scores to create a heat map
# getting similarity scores matrixes is at the bottom of lecture 13 

# need a for loop within a for loop. for each sequence in the list, get similarty score for each sequence
# need empty matrix that has the dimensions [n sequences:n sequences], to fill. likely need a counter for x and y positions
# use the aligned fasta, as the sequneces have already been aligned to each other
# to check, the diagonal should theoretically only contain the value 100, as comparing a sequence to itself


