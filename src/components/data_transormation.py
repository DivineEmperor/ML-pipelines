import os
import sys
sys.path.append('/Users/pavansaiguduru/Desktop/ML/ML_projects/Projets')
from src.exceptions import CustomException
from src.exceptions import CustomException
from src.logger import logging as logger

import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder


class DataTransformation:
    def __init__(self, train_data_features_path, test_data_features_path, train_data_labels_path, test_data_target_path):
        self.train_data_features_path = train_data_features_path
        self.test_data_features_path = test_data_features_path
        self.train_data_labels_path = train_data_labels_path
        self.test_data_target_path = test_data_target_path
        self.encoder = OneHotEncoder(sparse_output=False)

    def save_data(self,X_train, X_test, y_train, y_test):
        try:
            X_train.to_csv(self.train_data_features_path, index=False)
            X_test.to_csv(self.test_data_features_path, index=False)
            y_train.to_csv(self.train_data_labels_path, index=False)
            y_test.to_csv(self.test_data_target_path, index=False)
        except Exception as e:
            logger.error(f"Error saving data: {e}")
            raise CustomException("Error saving data",e)
        
    def onehot_encode(self, data, columns):
        self.encoder.fit_transform(data[columns])
        tranformed_df  = pd.DataFrame(self.encoder.transform(data[columns]), columns=self.encoder.get_feature_names_out(columns))
        data = data.drop(columns, axis=1)
        data = pd.concat([data, tranformed_df], axis=1)
        return data
    
    def clean_data(self, data):
        # data cleaning logic
        data = data.dropna()
        
    def transform_data(self, data):
        # data transformation logic
        X_train = pd.read_csv(self.train_data_features_path)
        X_test = pd.read_csv(self.test_data_features_path)
        y_train = pd.read_csv(self.train_data_labels_path)
        y_test = pd.read_csv(self.test_data_target_path)
        categorical_columns = [col for col in X_train.columns if X_train[col].dtype == 'object']
        X_train = self.onehot_encode(X_train,categorical_columns) 
        X_test = self.onehot_encode(X_test,categorical_columns)

        self.save_data(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    train_data_features_path = "artifacts/train/stud_features.csv"
    test_data_features_path = "artifacts/test/studt_features.csv"
    train_data_labels_path = "artifacts/train/stud_labels.csv"
    test_data_target_path = "artifacts/test/studt_target.csv"
    data_transformation = DataTransformation(train_data_features_path, test_data_features_path, train_data_labels_path, test_data_target_path)
    data = pd.read_csv("notebooks/data/stud.csv")
    data_transformation.transform_data(data)