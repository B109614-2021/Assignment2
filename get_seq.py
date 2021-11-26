#!/usr/local/bin/python3

# get protein family for query sequence
# get organism 
# get all sequences and save into a file

import os
import re
import sys
import subprocess
import shutil

### housekeeping, check for and remove relevant directories, and remake

# remove relevant directories if they exist 

try:
    shutil.rmtree('temp')
except OSError as e:
        # it is likely that temp does not exist, so don't want error to break the pipeline
        print("Error: %s : %s" % ('temp', e.strerror)) 

# create a directory to save temporary files in, so it is tidy and users can access different stages.

os.mkdir('temp')


### read in variables and test

# get subgroup

subgroup = input("please enter subgroup of interest:")

# print(subgroup)

# check that subgroup contains a non digit and has a length of at least 1
# keeps harassing the user until they enter some sort of string
# re.search will return a re.Match object if the pattern is found 

while(type(re.search(r'\D', subgroup)) != re.Match or len(subgroup) < 1)	:
        subgroup = input("variable subgroup must contain alphabetic characters, enter an organism or subgroup:")

# get protein

protein = input("please enter protein family of interest:")

# print(protein)

# check that protein contains a non digit, and has a length of at least 1
# keep harassing the user until something is entered 

while(type(re.search(r'\D', protein)) != re.Match or len(protein) < 1)       :
        protein = input("variable protein must contain alphabetic characters, enter a protein family:")

# get window size parameter for conservation as a variable, check it is a number, recommend 10

con_window_size = input("please enter a desired window size for conservation plot:")

# check this is an int
# keep harassing user until something is entered 

while(type(con_window_size) != int or length(con_window_size < 1):
	con_window_size = input("please enter an interger for the window size of the conservation plot:")

# Tell the user what they are searching for so they can maybe spot spelling mistakes

print("Searching for " + protein + " in " + subgroup )

### Check the number of found sequences

# check how many sequences there are. doing this before downloading sequneces prevents the user from downloading millions of sequences 
# tell users how many sequences have been found, if there are 0; stop, if there are > 1000; produce a warning, if greater than 2000, stop

esearch_seq_number_command = "esearch -db protein -query \"" + protein + " [PROTEIN] AND " + subgroup + " [ORGN]\" |efetch -format uid | wc -l"

try:
        os.system(esearch_seq_number_command)
        sequences_found = subprocess.check_output(esearch_seq_number_command, shell=True)
except OSError as e:
        # insert more descriptive error
        print("Error: esearch returned error")
	quit()

sequences_found = sequences_found.decode().replace("\n","")

print('search found ' + sequences_found + " sequences")

# if 0 sequences are found, tell the user and end the process

if int(sequences_found) == 0	:
	print("No sequences found")
	quit()

# if more than 1000 sequences found, but not too many more, warn the user 

if int(sequences_found) > 1000 and int(sequences_found) < 1500	:
	print("warning: more than 1000 sequences identifed, query may be too general")

# if more than 2000 sequences found, tell the user to be more specific. request may be too general.

if int(sequences_found) >= 1500:
	print("To many sequences, exiting program")
	quit()

### search for protein sequences

# big horrible looking command that is basically trying to make:
# esearch -db protein -query "$protein AND $subgroup [ORGN]" |efetch -format fasta > "$subgroup"_"$protein".fasta
# This can be used to get the desired protein sequences

esearch_command = "esearch -db protein -query \"" + protein + " [PROTEIN] AND " + subgroup + " [ORGN]\" |efetch -format fasta >  temp/" + subgroup + "_" + protein + ".fasta"

# run the command in python, check for errors
try:
	os.system(esearch_command)
	subprocess.call(esearch_command, shell=True)
except OSError as e:
	# insert more descriptive error
        print("Error: esearch returned error")
	quit()

# check if file is empty, indicating a problem with esearch, return an error is possible

input_file_name =  "temp/" + subgroup + "_" + protein + ".fasta" 

if os.stat(input_file_name).st_size == 0:
	print("No sequences found for " + protein + " in " + subgroup)
	quit()

# elif check the fist line of the file has >, indicating a fasta file
else	:
	print("Sequences downloaded") 


### list the species in the dataset 

# open fasta file, get the the line that has description using re.findall
# get the set of names
# make a file that has the sequence ID and species

all_species = []

with open(input_file_name , 'r') as my_file:
                file_data = my_file.read()

        # split into lines
        sequence_data = file_data.split("\n")

        # read the whole file line by line
        for line in sequence_data:
#               print(line)
		# extract the bit in brackets
                species = re.findall('\[.*\]', line)
#               print(species)
                all_species.extend(species)



### other checks
