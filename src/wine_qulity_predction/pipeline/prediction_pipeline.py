import  joblib
import numpy as np
import pandas as pd
from pathlib import Path

from src.wine_qulity_predction.entity.config_entity import ModelEvaluationConfig


class PredictionPipeline:
    def __init__(self):
        self.model=joblib.load(Path('artifacts/model_trainer/model.joblib'))


    def predict(self,data):
        prediction = self.model.predict(data)
        return prediction
