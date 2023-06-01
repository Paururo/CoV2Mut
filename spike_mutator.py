from Bio import SeqIO
import argparse
import os
import pandas as pd
import logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
'''
Command line: python spike_variant_generator.py -r /ruta/al/archivo/referencia.fasta -v /ruta/al/archivo/variantes_de_interes.txt -n nombre_de_salida.fasta -g Yes -s Yes
'''
def parse_args():
    parser = argparse.ArgumentParser(description = "Generate Spike with mutations")
    parser.add_argument("-r", dest = "reference_file", required = True, help="Path to the reference file")
    parser.add_argument("-v", dest = "variant_list", required = True, help="Path to the variant list file")
    parser.add_argument("-n", dest = "name", required = True, help="Name of the output file")
    parser.add_argument("-g", dest = "gaps", required = True, choices=['Yes', 'No'], help="Remove gaps or not")
    parser.add_argument("-s", dest = "split", required = True, choices=['Yes', 'No'], help="Split multifasta file or not")
    return parser.parse_args()

def read_file(path_to_file):
    if not os.path.isfile(path_to_file):
        logging.error(f"The file {path_to_file} does not exist.")
        return None

    try:
        with open(path_to_file, 'r') as file:
            return file.read()
    except IOError as e:
        logging.error(f"Unable to read file {path_to_file}: {str(e)}")
        return None

def read_referencefasta(path_to_file):
    fasta_str = read_file(path_to_file)
    if fasta_str:
        for record in SeqIO.parse(fasta_str, 'fasta'):
            return str(record.seq)
        logging.error(f"No valid FASTA records found in file {path_to_file}")
    return None

def read_file_tolist(path_to_file):
    try:        
        df = pd.read_csv(path_to_file, comment='#', header=None)
    except pd.errors.EmptyDataError:
        logging.warning(f"No valid lines found in file {path_to_file}")
        return None
    return df[0].tolist()

def generate_Spike_sequence(reference, list_positions):
    mutations = {int(pos.split("\t")[0]): pos.split("\t")[1] for pos in list_positions}
    spike_fasta = ""
    for count, base in enumerate(reference, start=1):
        if 21563 <= count <= 25384:
            spike_fasta += mutations.get(count, base)
    return spike_fasta

def generate_multifasta(list_process_files, output_file, reference, remove_gaps):
    with open(output_file, "w") as out_file:
        out_file.write(f">Wuhan_reference\n{str(reference[21562:25384])}\n")
        for element in list_process_files:
            fasta_name, file_name = element.split("\t")
            filepos_name = os.path.join(os.getcwd(), "positions", file_name)
            list_positions = read_file_tolist(filepos_name)
            spike_seq = generate_Spike_sequence(reference, list_positions)
            if remove_gaps == 'Yes':
                spike_seq = spike_seq.replace("-", "")
            out_file.write(f">{fasta_name}\n{spike_seq}\n")

def split_multifasta(decision, output_file):
    if decision.lower() == "yes":
        current_dir = os.getcwd()
        new_dir = os.path.join(current_dir, f"fastafiles_{output_file}")
        os.makedirs(new_dir, exist_ok=True)

        outfile = None
        with open(output_file, 'r') as infile:
            for line in infile:
                if line.startswith('>'):
                    if outfile is not None:
                        outfile.close()
                    outfile_path = os.path.join(new_dir, line.strip().lstrip('>') + '.fasta')
                    outfile = open(outfile_path, 'w')
                if outfile is not None:
                    outfile.write(line)
            if outfile is not None:
                outfile.close()

def main():
    args = parse_args()
    reference = read_referencefasta(args.reference_file)
    list_process_files = read_file_tolist(args.variant_list)
    generate_multifasta(list_process_files, args.name, reference, args.gaps)
    split_multifasta(args.split, args.name)

if __name__ == "__main__":
    main()
