import pickle
import os

# Load the model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'homePage', 'cox_model_top30.pkl')

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def predict(input_data):
    return model.predict([input_data]) 


import numpy as np

# We'll assume scikit-survival's Cox model
# has been loaded as `model`. E.g.:
# with open(MODEL_PATH, 'rb') as file:
#     model = pickle.load(file)

def predict_survival(input_data, model, time_horizon_days=3650):
    """
    Predict survival probability at `time_horizon_days` (default=10 years)
    using the Cox model from scikit-survival.
    
    :param input_data: list or array of feature values, shape (30,)
    :param model: the trained CoxPHSurvivalAnalysis model
    :param time_horizon_days: time in days to predict survival probability
    :return: float representing survival probability at the given time horizon
    """
    # Make sure input_data is 2D: shape (1, n_features)
    X = np.array(input_data).reshape(1, -1)

    # Predict the survival function
    surv_fn = model.predict_survival_function(X)  # returns array-like of step functions
    
    # surv_fn[0] is the step function for the single row
    # Evaluate at `time_horizon_days`
    prob_surv_10yr = float(surv_fn[0](time_horizon_days))  # e.g. 0.85 for 85%

    return prob_surv_10yr
