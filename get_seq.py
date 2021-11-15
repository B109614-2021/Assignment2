#!/usr/local/bin/python3

# get protein family for query sequence
# get organism 
# get all sequences and save into a file

import os
import sys

# section to read in variables 

try:
    os.rmdir('temp')
except OSError as e:
    print("Error: %s : %s" % ('temp', e.strerror))

subgroup = input("please enter subgroup of interest:")

# check that subgroup is a string
# keeps harassing the user until they enter some sort of string  

while(type(subgroup) != str or len(subgroup) < 1)	:
        subgroup = input("variable subgroup is empty, an organism or subgroup must be entered:")


protein = input("please enter protein family of interest:")

# check that protein is a string
# keep harassing the user until something is entered 

while(type(protein) != str or len(protein) < 1)       :
        protein = input("variable protein is empty, a protein family must be entered:")

# create a directory to save temporary files in, so it is tidy and users can access different stages.

os.mkdir(temp)

# insert variables into query, maybe have it so the input fasta has a name nade up of $subgroup and $protein 
 
# esearch -db protein -query "$protein AND $subgroup [ORGN]" |efetch -format fasta > "$subgroup"_"$protein".fasta


# if no file is returned, or the file is empty, or an error is returned, or the first line of input.fasta is errors then exit script
 
# call other scripts
