#!/bin/bash

# get protein family for query sequence
# get organism 

# get all sequences and save into a file 
esearch -db protein -query "glucose-6-phosphatase AND Aves [ORGN]" |efetch -format fasta > input.fasta
 
