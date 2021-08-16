import pandas as pd
from sklearn.model_selection import train_test_split
from models import BaseModel, PlpredSVM, PlpredNN, PlpredRF, PlpredGB
import argparse
 
def train_model(path:str, model: BaseModel) -> BaseModel:
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

    df = pd.read_csv(path)
    X = df.drop(['membrane'], axis=1)
    y = df['membrane']

    X_train, X_test, y_train, y_test = train_test_split(X,y)

    model.fit(X_train,y_train)
    report = model.validate(X_test, y_test)
    
    return model, report

def main():
    
    models = {  'neural_network': PlpredNN(), 
                'svm': PlpredSVM(), 
                'randon_forest': PlpredRF(), 
                'gradient_boosting': PlpredGB()
                }
    
    argument_parser = argparse.ArgumentParser(description='plpred-train: model training tools')
    argument_parser.add_argument('-p', '--processed_dataset', required=True, help='dataset processed path')
    argument_parser.add_argument('-o', '--output', required=True, help='path to output trained model (.pickle)')
    argument_parser.add_argument('-r', '--report', default=False, action= 'store_true', help='dataset processed path')
    argument_parser.add_argument('-m', '--model', required=True, default='randon_forest', choices=['neural_network', 'svm', 'randon_forest', 'gradient_boosting'],  help='Model to be selected')
    
    arguments = argument_parser.parse_args()

    model, report = train_model(path=arguments.processed_dataset, model=models[arguments.model])

    model.save(arguments.output)

    if arguments.report:
        print(report)


if __name__ == '__main__':
    main()
