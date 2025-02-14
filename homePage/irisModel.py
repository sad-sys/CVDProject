import pickle
import os

# Load the model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'homePage', 'irisModel.pkl')

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def predict(input_data):
    return model.predict([input_data]) 
