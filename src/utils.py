import os
import sys
import dill
import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    """
    Saves an object to a specified file path using dill.

    :param file_path: Path where the object should be saved.
    :param obj: Object to be saved.
    """
    try:
        # Create directory if it doesn't exist
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        # Saving the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    """
    Evaluates given models using GridSearchCV and returns their performance scores.

    :param X_train, y_train: Training data and labels.
    :param X_test, y_test: Test data and labels.
    :param models: Dictionary of models to evaluate.
    :param params: Dictionary of parameters for each model.
    :return: Dictionary of model names and their evaluation scores.
    """
    try:
        report = {}
        for model_name, model in models.items():
            model_params = params[model_name]

            # Grid search for best parameters
            gs = GridSearchCV(model, model_params, cv=3)
            gs.fit(X_train, y_train)

            # Fitting model with best parameters
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predicting and scoring the model
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            logging.info(f"{model_name}, Train model score: {train_model_score}, Test model score: {test_model_score}")

            report[model_name] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Loads an object from a specified file path using dill.

    :param file_path: Path of the file to load the object from.
    :return: Loaded object.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
