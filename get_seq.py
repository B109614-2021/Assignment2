#!/usr/local/bin/python3

# get protein family for query sequence
# get organism 
# get all sequences and save into a file

import os
import sys
import subprocess
import shutil

# section to read in variables 

try:
    shutil.rmtree('temp')
except OSError as e:
	# it is likely that temp does not exist, so don't want error to break the pipeline 
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

os.mkdir('temp')

# big horrible to look at text that is basically trying to make:
# esearch -db protein -query "$protein AND $subgroup [ORGN]" |efetch -format fasta > "$subgroup"_"$protein".fasta
# by inserting the python variables

esearch_command = "esearch -db protein -query \"" + protein + " AND " + subgroup + " [ORGN]\" |efetch -format fasta >  temp/" + subgroup + "_" + protein + ".fasta"

# insert variables into query, maybe have it so the input fasta has a name nade up of $subgroup and $protein 

print("Searching for " + protein + " in " + subgroup )

# run the command in python, check for errors
#### FIX THIS, ERRORS getting through as esearch tries multiple times. maybe use quietly 

try:
	os.system(esearch_command)
	subprocess.call(esearch_command, shell=True)
except OSError as e:
	# insert more descriptive error
        print("Error: esearch returned error")

# if no file is returned, or the file is empty, or an error is returned, or the first line of input.fasta is errors then exit script

# check file is empty

input_file_name =  "temp/" + subgroup + "_" + protein + ".fasta" 

if os.stat(input_file_name).st_size == 0:
	print("No sequences found for " + protein + " in " + subgroup)
else	:
	print("Sequences downloaded, beginning processing") 
# call other scripts
