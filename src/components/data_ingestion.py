import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    # Dataclass is used for simple data structures without methods
    train_data_path: str = os.path.join('data', 'train.csv')
    test_data_path: str = os.path.join('data', 'test.csv')
    raw_data_path: str = os.path.join('data', 'student_data.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion process")
        try:
            # Reading the dataset
            df = pd.read_csv('Data_Analysis/data/stud.csv')
            logging.info('Dataset loaded into DataFrame')

            # Creating directories if they don't exist
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

            # Saving the raw data
            df.to_csv(self.config.raw_data_path, index=False, header=True)

            # Splitting the dataset into training and testing sets
            logging.info("Performing train-test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving the train and test sets
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed successfully")

            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

def main():
    # Data Ingestion
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    # Data Transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    # Model Training
    model_trainer = ModelTrainer()
    accuracy = model_trainer.initiate_model_trainer(train_arr, test_arr)
    print(f"Model accuracy: {accuracy}")

if __name__ == "__main__":
    main()
