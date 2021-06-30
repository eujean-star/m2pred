
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
import pickle
import pandas as pd

class PlpredModel:
    version = '0.1'
    
    def __init__(self, estimator:BaseEstimator=RandomForestClassifier()) -> None:
        '''
        Initialize the instance/object

        Parameters
        ---------
        estimator: BaseEstimator
            A sckit learn model
        
        Returns:
        -------
            None
        '''
        self.estimator = estimator
    
    def fit(self, X:pd.DataFrame, y:pd.Series) -> None:
        '''
        Fits the estimator to the respectives dataframes

        Parameters:
        -----------
        X: X_train dataframe
        y: y_train, cotains the target label

        Returns:
        -------
        None
        '''
        self.estimator.fit(X, y)

    def predict(self, X):
  
        '''
        Generates a prediction base on fitted model.

        Parameters
        ==========
        x: pd.DataFrame
                features
        Returns
        =======
            y_pred = array
                Prediction of X.
        '''
        return self.estimator.predict(X)

    def validation(self, X_test, y_test):
        '''
        Validates the model using test data.
        
        Parameters
        ==========
        X_test: pd.DataFrame
            features
        y_test: pd.Series
            labels
        
        Returns
        =======
        report: str
            report the main classification metrics.
        '''
       
        y_pred = self.predict(X_test)
        return classification_report(y_test, y_pred)
    
    def save(self, file_path:str) -> None:
        '''
        saves the model in a pickle format.

        Parameters
        ==========
        file_path: str
            output path
        
        Returns
        ========
            None
        '''
        with open(file_path, 'wb') as handle:
            pickle.dump(self, handle)