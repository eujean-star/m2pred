
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import pandas as pd
import pickle

class BaseModel:
    version = '0.1'
    
    def __init__(self, estimator:BaseEstimator=GradientBoostingClassifier()) -> None:
        self.estimator = estimator
    
    def fity(self, X, y) -> None:
        self.estimator.fit(X, y)

    def predict(self, x) -> None:
        return self.estimator.predict(x)

    def validation(self, X_test, y_test):
        y_pred = self.predict(X_test)
        report = classification_report(y_test, y_pred)
        return report
    
    def save(self, file_path:str) -> None:
        with open(file_path, 'wb') as handle:
            pickle.dump(self, handle)
