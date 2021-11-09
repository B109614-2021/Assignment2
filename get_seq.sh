#!/bin/bash

# get protein family for query sequence
# get organism 

# get all sequences and save into a file
# Potentially change file name to use protein and species, so not just input.fasta
 
esearch -db protein -query "glucose-6-phosphatase AND Aves [ORGN]" |efetch -format fasta > input.fasta
 
# call other scripts
