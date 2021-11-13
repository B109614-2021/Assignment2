#!/bin/bash

# get protein family for query sequence
# get organism 
# get all sequences and save into a file

# section to read in variables 

echo 'please enter subgroup of interest:'
read subgroup

# check that $subgroup is a string
# if not a string return an error 

echo 'please enter protein family of interest:'
read protein

# check that $protein is a string
# if not a string return an error

while [-z "$protein"]; then
	echo "variable protein is empty, a protein family must be entered:"
	read protein 
done



# create a directory to save temporary files in, so it is tidy and users can access different stages.

# insert variables into query, maybe have it so the input fasta has a name nade up of $subgroup and $protein 
 
esearch -db protein -query "glucose-6-phosphatase AND Aves [ORGN]" |efetch -format fasta > input.fasta


# if no file is returned, or the file is empty, or an error is returned, or the first line of input.fasta is errors then exit script
 
# call other scripts
