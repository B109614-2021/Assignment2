#!/urs/local/bin/python3

# import packages 

import string
import sys
import os
import numpy as np
import pandas as pd

### use file_type to build up a command for clustalo



### run clustalo

# use clustalo to align
# plotcon can be used to plot the conservation
# plotcon -sequences aligned_test.fasta -graph svg probably best.  
# produces a line graph showing the regions with high conservation

### need to put in python script os.systemcall()
### need to make general
### need to let user pick whether they want to use complete, partial or predicted
### need to check for species number and ask user if they want to check within or between species (why not both!)
### need to pass variables from one script to another

# clustalo -i test.fasta -o aligned_test.fasta -v produces alignment file, can have set max number of sequences and max sequence length

# clustalo --percent-id --full-iter -i test.fasta -o aligned_test.fasta -v --force --clustering-out=cluster.txt. percent id doesnt seem to do anything, cluster.txt is confusing 


### run plotcon

# plotcon -sequences aligned_test.fasta -winsize 10 -graph svg. winsize 10 makes nicer looking graph than smaller numbers, but still contains information  

# need to return to screen as well as an svg
# add graph variables to make pretty
 
# "-graph" associated qualifiers
#   -gprompt            boolean    Graph prompting
#   -gdesc              string     Graph description
#   -gtitle             string     Graph title
#   -gsubtitle          string     Graph subtitle
#   -gxtitle            string     Graph x axis title
#   -gytitle            string     Graph y axis title
#   -goutfile           string     Output file for non interactive displays
#   -gdirectory         string     Output directory

