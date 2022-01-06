from sklearn.base import BaseEstimator
from models.base import BaseModel
from sklearn.neural_network import MLPClassifier

class PlpredNN(BaseModel):

    def __init__(self) -> BaseEstimator:
        self.estimator = MLPClassifier()
