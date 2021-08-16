from sklearn.base import BaseEstimator
from models.base import BaseModel
from sklearn.svm import SVC

class PlpredSVM(BaseModel):
    def __init__(self) -> BaseEstimator:
        self.estimator = SVC()