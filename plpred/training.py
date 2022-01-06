from sklearn.model_selection import train_test_split
from plpred.models import PlpredRF
from plpred.models import BaseModel
from plpred.models import PlpredNN
from plpred.models import PlpredSVM
import pandas as pd
import argparse
 

 #Atualizar a documentação. 
def train_model(preprocessed_csv:str, output, model=BaseModel) -> BaseModel:
    
    '''
    Train a machine learning model to classify membrane proteins.

    Parameters:
    ==========
    file_path: str
        path to the preprocessed dataset.
    
    Returns:
    =======
    model: PlpredModel
    '''

    df = pd.read_csv(preprocessed_csv)
    X = df.drop(['membrane'], axis=1)
    y = df['membrane']

    X_train, X_test, y_train, y_test = train_test_split(X,y)
    model.fity(X=X_train, y=y_train)
    report = model.validation(X_test, y_test)
    
    return model, report
    
def main():
    
    models = {'random_forest': PlpredRF(), 'neural_network': PlpredNN(), 'SVM': PlpredSVM()}

    parser = argparse.ArgumentParser(prog='Plpred-training', 
                                    usage= '''
        You should input the dataframe processed, also you have to explicit the path to save final archive
        as standard model,Random-forest will be performed. report if True, output model choosen reports''',
                                    description='Model training: training model with dataset preprocessed' )
    
    
    parser.add_argument( '-i', '--input', required=True, help='Introduce file path' )
    parser.add_argument( '-o', '--output', required=True, help='output Format (.PICKLE)' )
    parser.add_argument( '-r', '--report', default=False, action='store_true', help='show report classification' )
    parser.add_argument( '-a', '--algoritmo', default='random_forest',choices=['random_forest', 'neural_network', 'SVM' ] )
    args = parser.parse_args()
    

    model, report = train_model(preprocessed_csv=args.input, output=args.output, model=models[args.algoritmo])
    model.save(args.output)
    if args.report:
        print(report)

if __name__ == '__main__':
    main()     