#!/usr/local/bin/python3

### options:
# calculate GC% 
# plot and compare amino acid sequence/features. even if the underlying sequence is the same are the regions of hydrophobicity etc the same? Pepinfo or Pepwindow
# make some sort of plot comaring regions and their charge, which is most common in each region?

# pepwindow makes a hydropathy plot 
# pepinfo checks for different peptide properties at each position. Could use to make my own hydropathy plot 

# get numpy to make a matrix 
import numpy as np

input_file = 'aligned_test.fasta'

### get sequences 


### build empty similarity matrix, should have the same length as there are sequences 


### for loop of building a similarity score	

# paste seq and comparison seq together

# make empty matrix to calculate identity
# IDmatrix = np.eye(len(myseqs),dtype=int)

# make a counter for the sequence matrix 
# xcounter=0


# create a matrix comparing the similarity between each base 
# for xbase in myseqs :
#    xcounter+=1
#    ycounter=0
#    for ybase in myseqs :
#      ycounter+=1
#      print(xcounter,ycounter,xbase,ybase)
#      if ybase==xbase :
#        IDmatrix[(xcounter-1),(ycounter-1)]=1

# print(IDmatrix[0:18,0:18])

# as using the aligned version, the sequences should have the same length. therefor take the diagonal from the halfway point
# IDmatrix[0:9,9:18].diagonal()

# count the number of positives and divide by the length 
# print("The similarity was",int((IDmatrix[0:9,9:18].diagonal().sum()/9)*100),"percent")
# take this similarity value and add to a matrix, for position seq, comparison seq


### make a dendrogram out of sequence similarity. could label with id, and then use ID_species.csv to colour by species. 

# are sequences from the same species clustered? 


# for each sequence, get its similarity score to other sequences in the group, add a row of percent similarity to sequences to a growing matrix
# use these similarity scores to create a heat map
# getting similarity scores matrixes is at the bottom of lecture 13 

# need a for loop within a for loop. for each sequence in the list, get similarty score for each sequence
# need empty matrix that has the dimensions [n sequences:n sequences], to fill. likely need a counter for x and y positions
# use the aligned fasta, as the sequneces have already been aligned to each other
# to check, the diagonal should theoretically only contain the value 100, as comparing a sequence to itself


