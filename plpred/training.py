from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from models import PlpredRF
from models import BaseModel
from models import PlpredNN
import pandas as pd
import argparse
import pickle
 
def train_model(preprocessed_csv:str, output, model=None):
    
    '''
    Train a machine learning model to classify membrane proteins.

    Parameters:
    ==========
    file_path: str
        path to the preprocessed daaset.
    
    Returns:
    =======
    model: PlpredModel
    '''
    df = pd.read_csv(preprocessed_csv)
    X = df.drop(['membrane'], axis=1)
    y = df['membrane']

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    model.fit(X_train,y_train)
    report = model.validation(X_test, y_test)
    print('Modelo selecinado:', model)
    print(report)

    model.save(output)
    


def main():
    parser = argparse.ArgumentParser(description='Model Selecion')
    parser.add_argument('--model', required=True, help='selection of model')
    parser.add_argument('-i', '--input',required=True, help='Introduce file path')
    parser.add_argument('-o', '--output',required=True, help='output dormat')
    args = parser.parse_args()
    
    #nao to conseguindo passar o modelo como parametro pro argparser
    if args.model == 'PlpredRF':
        train_model(preprocessed_csv=args.input, output=args.output, model=PlpredRF())
        print('modelo seleciona:', args.model)

if __name__ == '__main__':
    main()     