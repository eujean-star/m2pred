from models.base import BaseModel
from sklearn.ensemble import GradientBoostingClassifier

class PlpredGB(BaseModel):

    def __init__(self):
        self.estimator = GradientBoostingClassifier()

        
