from os import path
from Bio import SeqIO
from Bio.SeqUtils import ProtParam
import pandas as pd
import argparse

def compute_aa(protein_seq:str) -> dict:
    """
    Compute aminoacids composition of a given protein sequence

    parameters
    ==========
    protein_sequence: str
        sequence of the protein to be processed.
    
    Returns
    =======
    aa_composition: dict
        dictionary containing the relative abundance of each aminoacid.
    
    """
    analyzer = ProtParam.ProteinAnalysis(str(protein_seq))
    aa_composition = analyzer.get_amino_acids_percent()
    return aa_composition
''' Criação do dataframe com os dados'''
def generate_aa_compostion_df(file_path:str, membrane_label:int):
    
    df = pd.DataFrame()
    handle = open(file_path)
    parser = SeqIO.parse(handle, 'fasta')
    
    for protein in parser:
        protein_data = compute_aa(protein.seq)        
        protein_data['membrane'] = membrane_label
        df = df.append([protein_data], ignore_index=False)
    
    return df

def main():
    argument_parser = argparse.ArgumentParser(description='plpred-preprocess: Data processing tool')

    argument_parser.add_argument('-m', '--membrane_proteins', required=True, help='Path to membrane file location (.fasta)' )
    argument_parser.add_argument('-c', '--cytoplasm_proteins', required=True, help='Path to citoplasm file location (.fasta)' )
    argument_parser.add_argument('-o', '--output_file', required=True, help='Path to destination of file of both files mergeded' )
    argument = argument_parser.parse_args()

    df_membrane = generate_aa_compostion_df(argument.membrane_proteins, membrane_label=1   )
    df_cytoplasm = generate_aa_compostion_df(argument.cytoplasm_proteins, membrane_label=0 )
    df_processed = pd.concat([df_membrane, df_cytoplasm])
    df_processed.to_csv(argument.output_file, index=False)
    

    argument = argument_parser.parse_args()


if __name__ == "__main__":
    main()