from plpred.preprocessing import generate_aa_compostion_df, compute_aa
from Bio import SeqIO
import pandas as pd
import argparse
import pickle



def run_model(path, model_path) -> pd.DataFrame:
    '''
    'Run_model' will execute the prediction to some fasta file 
    
    Parameters:
    ----------
        Path:str
            Protein sequence (.fasta)
        
        Model_path:
            Model choosen to perform prediction.


    Returns:
    -------
    Dataframe pandas object
    
    '''

    with open(model_path, 'rb') as handle:
        model = pickle.load(handle)

    handle = open(path)
    parser = SeqIO.parse(handle, 'fasta')

    df_aa_comp = pd.DataFrame()
    df_pred = pd.DataFrame(columns=['id', 'membrane']) 

    for record in parser:
        aa_composition = compute_aa(str( record.seq ))
        aa_composition['id'] = record.id
        df_aa_comp = df_aa_comp.append(aa_composition, ignore_index=True)

    ids = df_aa_comp['id']
    X = df_aa_comp.drop(['id'], axis=1)
    y_pred = model.predict(X)

    df_pred['id'] = ids
    df_pred['membrane'] = y_pred

    return df_pred

def main():
    argument = argparse.ArgumentParser(prog='Predicting protein location', 
    description='Model predict: Use a model trained to predict the interesting label')
    
    argument.add_argument('-i', '--input', required=True, help='input file (.fasta)')
    argument.add_argument('-o', '--output', required=True, help='output file (.csv)')
    argument.add_argument('-m', '--model', required=True, help='Trained model (.pickle)')
    argument = argument.parse_args()

    predicting = run_model( path=argument.input, model_path=argument.model )
    predicting.to_csv(argument.output, index=False)
    



if __name__ == '__main__':
    main()

