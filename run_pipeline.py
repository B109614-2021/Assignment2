#!/usr/local/bin/python3

### this script call and runs the other scripts 

# download and save sequences into a fasta file
exec(open("get_seq.py").read())

print(input_file_name)

# check which species are present and how many of each
exec(open("check_species.py").read())

print(sequence_type)

# exec(open("check_AA_sequence.py").read())

# split into partial, predicted and complete sequences, then calculate conservation 
exec(open("split_into_sequence_type.py").read())

