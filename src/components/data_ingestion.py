import os
import sys
sys.path.append('/Users/pavansaiguduru/Desktop/ML/ML_projects/Projets')
from src.exceptions import CustomException
from src.exceptions import CustomException
from src.logger import logging as logger

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transormation import DataTransformationConfig
from src.components.data_transormation import DataTransformation

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    data_path: str = "notebooks/data/stud.csv"
    test_data_features_path: str = "artifacts/test/studt_features.csv"
    test_data_target_path: str = "artifacts/test/studt_target.csv"
    train_data_features_path: str = "artifacts/train/stud_features.csv"
    train_data_labels_path: str = "artifacts/train/stud_labels.csv"
    test_size: float = 0.2
    random_state: int = 42
    target_column: str = 'math_score'


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.config.data_path)
            

        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise CustomException("Error loading data",e)

    def split_data(self):
        try:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.data.drop(self.config.target_column, axis=1),
                self.data[self.config.target_column],
                test_size=self.config.test_size,
                random_state=self.config.random_state
            )
        except Exception as e:
            logger.error(f"Error splitting data: {e}")
            raise CustomException("Error splitting data",sys)


    def save_data(self):
        try:
            
            self.X_train.to_csv(self.config.train_data_features_path, index=False)
            self.X_test.to_csv(self.config.test_data_features_path, index=False)
            self.y_train.to_csv(self.config.train_data_labels_path, index=False)
            self.y_test.to_csv(self.config.test_data_target_path, index=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
            raise CustomException("Error saving data",sys)
    
    def make_config_dir(self):
        try:
            os.makedirs(os.path.dirname(self.config.test_data_target_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.config.test_data_target_path), exist_ok=True)
        except Exception as e:
            logger.error(f"Error creating directories: {e}")
            raise CustomException("Error creating directories",sys)


    def ingest_data(self):
        self.load_data()
        self.split_data()
        self.make_config_dir()
        self.save_data()

        return (
            self.config.train_data_features_path,
            self.config.train_data_labels_path,
            self.config.test_data_features_path,
            self.config.test_data_target_path
        )



if __name__ == "__main__":
    config = DataIngestionConfig()
    data_ingestion = DataIngestion(config)
    xtr,ytr,xt,yt = data_ingestion.ingest_data()

    data_tranformer = DataTransformation()
    xtr,ytr,xt,yt,pre_processing_obj  = data_tranformer.initiate_data_transformation(xtr,ytr,xt,yt)
    # print(len(xtr),len(ytr),len(xt),len(yt))
    # print(xtr.shape,ytr.shape,xt.shape,yt.shape)
    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(xtr,ytr,xt,yt))

