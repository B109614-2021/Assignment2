#!/usr/local/bin/python3

# get protein family for query sequence
# get organism 
# get all sequences and save into a file

import os
import re
import sys
import subprocess
import shutil

# section to read in variables 
# regular expresssion, \d means digit. \D is non digit. check there is at least 1 non digit?


try:
    shutil.rmtree('temp')
except OSError as e:
	# it is likely that temp does not exist, so don't want error to break the pipeline 
	print("Error: %s : %s" % ('temp', e.strerror))

subgroup = input("please enter subgroup of interest:")

# check that subgroup is a string
# keeps harassing the user until they enter some sort of string  

while(re.search(r'\D', subgroup) != True or len(subgroup) < 1)	:
        subgroup = input("variable subgroup must contain alphabetic characters, enter an organism or subgroup:")


protein = input("please enter protein family of interest:")

# check that protein is a string
# keep harassing the user until something is entered 

while(re.search(r'\D', protein) != True or len(protein) < 1)       :
        protein = input("variable protein must contain alphabetic characters, enter a protein family:")

# create a directory to save temporary files in, so it is tidy and users can access different stages.

os.mkdir('temp')

# big horrible to look at text that is basically trying to make:
# esearch -db protein -query "$protein AND $subgroup [ORGN]" |efetch -format fasta > "$subgroup"_"$protein".fasta
# by inserting the python variables

esearch_command = "esearch -db protein -query \"" + protein + " AND " + subgroup + " [ORGN]\" |efetch -format fasta >  temp/" + subgroup + "_" + protein + ".fasta"

# tell the user what they are searching for, maybe they spot a spelling mistake 

print("Searching for " + protein + " in " + subgroup )

# run the command in python, check for errors
#### FIX THIS, ERRORS getting through as esearch tries multiple times. maybe use quietly 
# this is done quietly. it is possible that an errors will be printed to the screen as part of subprocess
# these will be picked up as the output file will be empty

try:
	os.system(esearch_command)
	subprocess.call(esearch_command, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
except OSError as e:
	# insert more descriptive error
        print("Error: esearch returned error")

# check if file is empty, indicating a problem with esearch, return an error is possible

input_file_name =  "temp/" + subgroup + "_" + protein + ".fasta" 

if os.stat(input_file_name).st_size == 0:
	print("No sequences found for " + protein + " in " + subgroup)
	# exit pipeline if file is empty
# elif check the fist line of the file has >, indicating a fasta file
else	:
	print("Sequences downloaded, beginning processing") 


# call other scripts
