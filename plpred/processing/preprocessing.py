from Bio import SeqIO
from Bio.SeqUtils import ProtParam
import pandas as pd

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


if __name__ == "__main__":
   
    df_membrane = generate_aa_compostion_df('data/raw/membrane.fasta', membrane_label=1)
    df_cytoplasm = generate_aa_compostion_df('data/raw/cytoplasm.fasta', membrane_label=0)
    df_final = pd.concat([df_membrane, df_cytoplasm])
    
    
    df_final.to_csv('data/processed/data_processed.csv', index=False)
    print('Salvo com sucesso')
