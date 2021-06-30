from Bio import SeqIO
from Bio.SeqUtils import ProtParam
import pandas as pd

def compute_aa(protein_seq:str) -> dict:
    """
    Compute aminoacids composition of a given protein sequence

    Parameters
    ==========
    protein_sequence: str
        Protein's sequence that must be processed.
    
    Returns
    =======
    aa_composition: dict
        Dictionary containing the relative abundance of each aminoacid.
    """
    
    
    analyzer = ProtParam.ProteinAnalysis(str(protein_seq))
    aa_composition = analyzer.get_amino_acids_percent()
    return aa_composition

def generate_aa_compostion_df(file_path:str, membrane_label:int) -> pd.DataFrame:
    
    '''
    > Return a DataFrame with the relative abundance of each aminoacid < .

    Parameter:
    =========
    File_path:str
        Requires file path to be processed. 
    
    Membrane_label:int
        If 1, indicates that protein it's from membrane, else: it's from cytoplasm
    
    Returns: pd.Dataframe
    =====================
        pandas DataFrame
    '''
    
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
    print('Unindo os datasets')
    df_final = pd.concat([df_membrane, df_cytoplasm])
    df_final.to_csv('data/processed/data_processed.csv', index=False)
    print('Salvo com sucesso')