#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Bio import SeqIO
import argparse
import os
import subprocess
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def read_referencefasta(path_to_file):
    if not os.path.isfile(path_to_file):
        logging.error(f"The file {path_to_file} does not exist.")
        return None

    with open(path_to_file, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            return str(record.seq)

    logging.error(f"The file {path_to_file} does not contain any FASTA records.")
    return None

def parse_args():
    parser = argparse.ArgumentParser(description = "Generate Spike protein sequences with mutations from provided reference sequence and variant list.")
    
    parser.add_argument("-r", "--reference_file", required=True,
                        help="Path to the FASTA file containing the reference sequence.")
    parser.add_argument("-v", "--variant_list", required=True,
                        help="Path to the list of variants of interest.")
    parser.add_argument("-n", "--name", required=True,
                        help="Desired name for the output file.")
    parser.add_argument("-g", "--gaps", action="store_true",
                        help="Include this flag to remove gaps in the output sequence(s).")
    parser.add_argument("-s", "--split", action="store_true",
                        help="Include this flag to split the output into separate FASTA files for each sequence.")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

if __name__ == 'main':
    main()