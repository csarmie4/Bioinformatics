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
sequences = (
    []
)  # Here we are setting up an array to save our sequences for the next step


def parsing(fasta_file_path):

    # Parsing through a fasta file
    for seq_record in SeqIO.parse(fasta_file_path, "fasta"):
        if count < 6:
            sequences.append(seq_record)
            print(
                "Id: "
                + seq_record.id
                + " \t "
                + "Length: "
                + str("{:,d}".format(len(seq_record)))
            )
            print(repr(seq_record.seq) + "\n")
            count = count + 1

    chr2L = sequences[0].seq
    chr2R = sequences[1].seq
    chr3L = sequences[2].seq
    chr3R = sequences[3].seq
    chr4 = sequences[4].seq
    chrM = sequences[5].seq

    return chr2L, chr2R, chr3L, chr3R, chr4, chrM


def parsing_optimized(fasta_file_path, max_records=6):

    count = 0

    with open(fasta_file_path, "r") as handle:
        for seq_record in SeqIO.parse(handle, "fasta"):
            if count < max_records:
                print(
                    "Id: "
                    + seq_record.id
                    + " \t "
                    + "Length: "
                    + str("{:,d}".format(len(seq_record)))
                )
                print(repr(seq_record.seq) + "\n")
                count += 1
            else:
                break

    chr2L = sequences[0].seq
    chr2R = sequences[1].seq
    chr3L = sequences[2].seq
    chr3R = sequences[3].seq
    chr4 = sequences[4].seq
    chrM = sequences[5].seq

    return chr2L, chr2R, chr3L, chr3R, chr4, chrM


messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print("Messenger RNA: " + messenger_rna)
print("Protein Sequence: " + messenger_rna.translate())
