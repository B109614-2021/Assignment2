#!/bin/bash

# run acommand via commandline to run a sequnece through PROSITE ie get  https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?seq=P98073
# can use sequence name to run it, which may be in the fasta file 
# use command GET, with the url attached to it.

# header from generated fasta is not valid for prosite  
# use wget, then link, with the sequence included in the seq section. ie wget https://prosite.expasy.org/cgi-bin/prosite/PSScan.cgi?seq=MIWVAVIGDWFNLIFKWILFGHRPYWWVQETMIYPNQSSPCLEQFPITCETGPGSPSGHAMGSSCVWYVM
# need to save output in a different format.

# then grep for motifs, count up number of motifs and produce both a file showing what motifs occur on each sequence, and a bar plot of the most common.


# can run wget throuhg python, and specify output with -O. for example subprocess.call('wget -qO eukaryotes.txt "ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt" ' , shell=True)

# use os.system to run bash commandline commands
