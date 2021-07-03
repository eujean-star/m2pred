from models.base_model import BaseModel
from sklearn import svm

class PlpredSVM(BaseModel):
    def __init__(self):
        self.estimator = svm