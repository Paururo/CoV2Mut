# CoV2SpikeMut
This is a Python script for generating SARS-CoV-2 spike protein sequences with specified mutations, given a reference sequence and a list of variants of interest.

_Spike Variant Generator_

## About

`CoV2SpikeMut` is a Python script specifically designed for generating spike protein sequences of SARS-CoV-2, including user-specified mutations. Given a reference sequence and a list of variants of interest, `CoV2SpikeMut` enables researchers to simulate mutated SARS-CoV-2 sequences, contributing to ongoing research in the field of viral genomics and the study of COVID-19.

## Installation

Clone this repository to your local machine using the following command:

```
git clone https://github.com/Paururo/CoV2SpikeMut.git
```

## Dependencies

CoV2SpikeMut depends on the following Python packages:

- Biopython
- pandas
- argparse
- os
- logging

Before running the script, please ensure these packages are installed in your Python environment. You can install these packages using pip:
```
pip install biopython pandas argparse
```
## Usage

To use CoV2SpikeMut, run the following command from your terminal:
```
python spike_variant_generator.py -r /path/to/reference.fasta -v /path/to/variants_of_interest.txt -n output_name.fasta -g yes -s yes
```
In this command:

    -r specifies the path to the reference sequence FASTA file.
    -v specifies the path to the text file containing variants of interest.
    -n specifies the output FASTA filename.
    -g decides whether to remove gaps ("-") in the sequences ("yes" to remove, "no" to retain).
    -s decides whether to split the output multi-FASTA file into individual FASTA files ("yes" to split, "no" to retain as single file).

Please replace the paths and filenames with the actual ones on your system.
## Contributing

We welcome contributions to CoV2SpikeMut! If you have a feature request, bug report, or proposal for improving the script, please open a new issue on GitHub issue tracker.

## Contact

If you have any questions, comments, or would like to get in contact, please open an issue on  GitHub issue tracker.
