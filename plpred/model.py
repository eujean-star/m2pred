
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import pandas as pd
import pickle

class PlpredModel:
    version = '0.1'
    
    def __init__(self, estimator:BaseEstimator=RandomForestClassifier()) -> None:
        self.estimator = estimator
    
    def fit(self, X, y) -> None:

        self.estimator.fit(X, y)

    def predict(self, X):
        return self.estimator.predict(X)

    def validation(self, X_test, y_test):
        y_pred = self.predict(X_test)
        return classification_report(y_test, y_pred)
    
    def save(self, file_path:str) -> None:
        with open(file_path, 'wb') as handle:
            pickle.dump(self, handle)

    
modelo = PlpredModel()
print(type(modelo.estimator))