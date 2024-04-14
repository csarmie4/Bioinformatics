import numpy as np
import pandas as pd 
import Bio

from Bio.Seq import Seq
from Bio import SeqIO

print("Biopython v", Bio.__version__)

my_seq = Seq("AGTACAVTGGT")
print(my_seq)

print(my_seq + " - Sequence")

# Since DNA has two strands, every DNA sequence has a complementary sequence running parallel. 
# In the complementary sequence, Adenine (A) is always paired with Thymine (T), 
# and Cytosine (C) is always paired with Guanine (G).
print(my_seq.complement() + " - Complement")
print(my_seq.reverse_complement() + " - Reverse Complement")


count = 0
sequences = [] # Here we are setting up an array to save our sequences for the next step

for seq_record in SeqIO.parse("S:/Bioinformatics/Biopython1/Tutorial/Data/genome.fa", "fasta"):
    if (count < 6):
        sequences.append(seq_record)
        print("Id: " + seq_record.id + " \t " + "Length: " + str("{:,d}".format(len(seq_record))) )
        print(repr(seq_record.seq) + "\n")
        count = count + 1