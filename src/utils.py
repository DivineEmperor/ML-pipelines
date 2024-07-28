import os
import pickle
from src.exceptions import CustomException
import sys
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    model_report = {}
    for model_name, model in models.items():
        try:
            gs = GridSearchCV(model, param[model_name], cv=3, n_jobs=-1)
            gs.fit(X_train, y_train)
            best_model_params = gs.best_params_
            model = model.set_params(**best_model_params)
            model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            model_report[model_name] = r2_score(y_test, y_test_pred)            
        except Exception as e:
            raise CustomException(e, sys)
    return model_report

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)
        return obj
    except Exception as e:
        raise CustomException(e, sys)
    