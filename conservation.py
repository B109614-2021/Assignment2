#!/urs/local/bin/python3

# script to check and plot (as a heatmap) the conservation between the sequences 
# potentially multiple sequences for each species? so could plot both conservation within a species.

# To check conservation, use numpy to create a matrix (Lecture 13, conditionals). Find percent conservation between sequences and make a heatmap. label with species

# check: does input files exist
# check: does it have more than one sequence
# check: does it have fewer than 1000 sequences? if so, give user the choice to either use first N sequences or exit (check they give an int less than 1001 or the string "exit")

# I think /localdisk/data/BPSM/Assignment2/pullseq can extract sequneces, so could be used to extract the desired number of sequences

# take input fasta file, and split into a list; one item for each sequence. (could potentiall make list of lists?)
# split into list for species, so get unique species names occuring in the list of lists, make a object for each species, containing all sequences


# as the sequences are large, may use clustalo to align
# plotcon can be used to plot the conservation  
