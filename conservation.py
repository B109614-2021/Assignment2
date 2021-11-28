#!/urs/local/bin/python3

# import packages 

import string
import sys
import os
import numpy as np
import pandas as pd

### use file_type to build up a command for clustalo

clustalo_command = "clustalo -i temp//" + sequence_type + "_sequences.fasta -o temp//" + sequence_type + "_aligned.fasta"

print(clustalo_command)

print("Calculating sequene conservation")

### run clustalo

# use clustalo to align
# plotcon can be used to plot the conservation
# plotcon -sequences aligned_test.fasta -graph svg probably best.  
# produces a line graph showing the regions with high conservation

# clustalo -i test.fasta -o aligned_test.fasta -v produces alignment file, can have set max number of sequences and max sequence length

# clustalo --percent-id --full-iter -i test.fasta -o aligned_test.fasta -v --force --clustering-out=cluster.txt. percent id doesnt seem to do anything, cluster.txt is confusing 

try:
        os.system(clustalo_command)
except OSError as e:
        # insert more descriptive error
        print("Error: clustalo returned error")
        quit()


### run plotcon

plotcon_command_svg = "plotcon -sequences temp//" + sequence_type + "_aligned.fasta -goutfile output//" + subgroup + "_" + protein + "_con_plot -winsize " + con_window_size + " -graph svg"

try:
        os.system(plotcon_command_svg)
except OSError as e:
        # insert more descriptive error
        print("Error: plotcon returned error")
        quit()

print("Printing conservation map to screen")

plotcon_command_screen = "plotcon -sequences temp//" + sequence_type + "_aligned.fasta -winsize " + con_window_size + " -graph x11"

try:
        os.system(plotcon_command_screen)
except OSError as e:
        # insert more descriptive error
        print("Error: plotcon returned error")
        quit()

print("plot conservation: Done")
