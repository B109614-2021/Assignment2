#!/usr/local/bin/python3

### options:
# calculate GC% 
# plot and compare amino acid sequence/features. even if the underlying sequence is the same are the regions of hydrophobicity etc the same? Pepinfo or Pepwindow
# make some sort of plot comaring regions and their charge, which is most common in each region?

# split into list for species, so get unique species names occuring in the list of lists, make a object for each species, containing all sequences

# get R python, so can make a heat map
# get numpy to make a matrix 
import numpy as np


# for each sequence, get its similarity score to other sequences in the group, add a row of percent similarity to sequences to a growing matrix
# use these similarity scores to create a heat map
# getting similarity scores matrixes is at the bottom of lecture 13 

# need a for loop within a for loop. for each sequence in the list, get similarty score for each sequence
# need empty matrix that has the dimensions [n sequences:n sequences], to fill. likely need a counter for x and y positions
# use the aligned fasta, as the sequneces have already been aligned to each other
# to check, the diagonal should theoretically only contain the value 100, as comparing a sequence to itself

