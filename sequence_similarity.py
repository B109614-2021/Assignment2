#!/usr/local/bin/python3

### import all of the packages and files
# get numpy to make a matrix 

import numpy as np
import os
import re
import sys
import subprocess
import shutil
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

aligned_input_file = 'temp/' + sequence_type + "_aligned.fasta"

with open(aligned_input_file , 'r') as my_file:
                aligned_sequence_data = my_file.read()

### get sequences from the file 

# need to split aligned_test.fasta into a list of sequences, removing the header
# split at <, readd <, remove lines starting with <?

sequence_data = aligned_sequence_data.split('>')

# create a dict to hold just ids and their matching sequences

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
		# print(protein_sequence[1])
		
		# save into a dict, with ID as the key 
		id_sequence[id] = protein_sequence[1]

# print(id_sequence)

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

# take this similarity value and add to a dataframe, for position seq, comparison seq

# test that the function works the same as the one in the lecture, returns 66 as expected
# similarity = cal_seq_sim('ATTGTACGG','AATGAACCG')
# print(similarity)

### get similarity values 

sequence_ids = list(id_sequence.keys())

print(sequence_ids)

headers = ['ID'] + sequence_ids

df = pd.DataFrame(columns = headers)

for key_of_interest in sequence_ids:
	
	# make a row for each key, comparing it to all the other keys 
	print(key_of_interest)
	similarity_list = [key_of_interest] 
	
	# calculate the similarity value for each sequence with 
	for key_contrast in sequence_ids:
	
		# use premade function to calculate sequence similarities 
		similarity_value = cal_seq_sim(id_sequence.get(key_of_interest), id_sequence.get(key_contrast))
		similarity_list.append(similarity_value)
	
	# print(similarity_list)
	df.loc[len(df)] = similarity_list


# print(df) dataframe has values of 100 on the diagonal. this is good and expected as the sequences are being compared with themselves on the diagonal 

# set the index to the id so this can be used for labelling
df = df.set_index('ID')

# calculate which sequences are most related to each other by this magic function 
Z = linkage(df, 'ward')

# create the dendrogram
dendrogram(Z, leaf_rotation=90, leaf_font_size=8, labels=df.index)

# save the dendrogram 

plt.show()
plt.savefig("output/sequence_similarity_tree.png",transparent=True, bbox_inches = 'tight', pad_inches=0.5)



# save the dataframe used incase a user is interested 
df.to_csv("temp/sequence_similarity_df.csv")

