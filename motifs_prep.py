#!/usr/local/bin/python3

# script to prep for using PROSITE database to identify motifs of interest

# load in input file

# check: does input files exist
# check: does it have more than one sequence
# check: does it have fewer than 1000 sequences? if so, give user the choice to either use first N sequences or exit (check they give an int less than 1001 or enter a string equal to exit)

# PROSITE is a big database where sequences can be given to it and it will return a list of matching domains. hopefully there is a function that will allow remote access


# check for non protein characters in the sequence, check if they match IUPAC ambiguity codes - Lecture 11 (hopefully PROSITE uses them). if not then remove.

