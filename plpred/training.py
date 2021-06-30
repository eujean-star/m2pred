from model import PlpredModel
import pandas as pd
#divisão dos dados em treino e teste.
from sklearn.model_selection import train_test_split
#modelo utilizado
from sklearn.ensemble import RandomForestClassifier
#classificação do modelo. 
from sklearn.metrics import classification_report
#redução de dimensionalidade
from sklearn.decomposition import PCA
#útil para salvar objetos do python em algum arquivos e é possivel utilizar o objeto depois. 
import pickle
 
def train_model(path:str) -> PlpredModel:
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

    model =  PlpredModel()
    model.fit(X_train,y_train)
    report = model.validation(X_test, y_test)
    
    print(report)
    return model

if __name__ == '__main__':
    from sklearn.ensemble import GradientBoostingClassifier
    
    model =  PlpredModel(estimator = GradientBoostingClassifier())
    model = train_model('data/processed/processed.csv')
    model.save('data/models/model.pickle')
        