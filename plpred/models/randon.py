from sklearn.base import BaseEstimator
from models.base import BaseModel
from sklearn.ensemble import RandomForestClassifier


class PlpredRF(BaseModel):
    
    def __init__(self) -> BaseEstimator:
        self.estimator = RandomForestClassifier()


