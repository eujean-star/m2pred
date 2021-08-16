from preprocessing import compute_aa
from Bio import SeqIO
import pandas as pd
import argparse
import pickle

def run_model(fasta_file_path, model_path) -> pd.DataFrame:
    '''
    Run a membrane protein predition from a FASTA file format

    Parameters
    ----------
    file_path: str
        Fasta file path to be used.

    model_path: str
        Trained model path in pickle format.

    '''

    with open(model_path, 'rb') as handle:
        model = pickle.load(handle)
    
    handle = open(fasta_file_path)
    parser = SeqIO.parse(handle, 'fasta')

    df_aa_composition = pd.DataFrame()
    df_predictions = pd.DataFrame(columns=['id', 'membrane'])

    for record in parser:
        aa_composition = compute_aa(str(record.seq))
        aa_composition['id'] = record.id
        df_aa_composition = df_aa_composition.append(aa_composition, ignore_index=True)

    X = df_aa_composition.drop(['id'], axis=1)
    ids = df_aa_composition['id']
    y_pred = model.predict(X)

    return df_predictions

def main():
    argument_parser = argparse.ArgumentParser(description='plpred-predict: subcelullar location predict tool')
    argument_parser.add_argument('-i', '--input', required=True, help='Path of .fasta file (.fasta)')
    argument_parser.add_argument('-o',  '--output', required=True, help= 'Path to output (.csv)')
    argument_parser.add_argument('-m', '--model', required=True, help='Trained model(.pickle)')
    arguments = argument_parser.parse_args()

    df_predictions = run_model(fasta_file_path=arguments.input, model_path=arguments.model)
    df_predictions.to_csv(arguments.output, index=False)

if __name__ == '__main__':
    main()
