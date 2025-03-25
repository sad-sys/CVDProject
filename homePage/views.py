from django.shortcuts import render
from .forms import PredictionForm
import pickle
import os
import numpy as np
from sksurv.functions import StepFunction

# Define the function to compute survival at 10 years (3650 days)
def predict_survival(input_data, model, time_horizon_days=365):
    X = np.array(input_data).reshape(1, -1)
    survival_function = model.predict_survival_function(X)
    # Get the survival probability at 10 years
    prob_surv_10yr = float(survival_function[0](time_horizon_days))
    return prob_surv_10yr

def predict_view(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MODEL_PATH = os.path.join(BASE_DIR, 'homePage', 'cox_model_top30.pkl')

    # Load the model
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)

    result = None  # Default result

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract all 30 fields from form.cleaned_data, in the correct order
            input_data = [
                # Boolean fields (converted to int: True → 1, False → 0)
                int(form.cleaned_data['CAD_at_base']),
                int(form.cleaned_data['ts_Vascular_heart_problems_diagnosed_by_doctor_Instance_0_1']),
                int(form.cleaned_data['pmh_Merged_ICD_Z39']),
                int(form.cleaned_data['ts_Current_tobacco_smoking_Instance_0_0']),
                int(form.cleaned_data['ts_Type_of_tobacco_currently_smoked_Instance_0_neg7']),
                int(form.cleaned_data['ts_Type_of_tobacco_currently_smoked_Instance_0_3']),
                int(form.cleaned_data['ISS_at_base']),
                int(form.cleaned_data['ts_Type_of_accommodation_lived_in_Instance_0_neg7']),
                int(form.cleaned_data['ts_Type_of_accommodation_lived_in_Instance_0_5']),
                int(form.cleaned_data['ts_Ethnic_background_Instance_0_4003']),
                int(form.cleaned_data['qrisk_Ethnic_background_Instance_0_4003']),
                int(form.cleaned_data['nhc_Ethnic_background_Instance_0_4003']),
                int(form.cleaned_data['ts_Type_of_accommodation_lived_in_Instance_0_3']),
                int(form.cleaned_data['ts_Type_of_accommodation_lived_in_Instance_0_4']),
                int(form.cleaned_data['ts_Type_of_tobacco_currently_smoked_Instance_0_1']),
                int(form.cleaned_data['ts_Type_of_accommodation_lived_in_Instance_0_1']),
                int(form.cleaned_data['ts_Type_of_accommodation_lived_in_Instance_0_2']),
                int(form.cleaned_data['ts_Type_of_tobacco_currently_smoked_Instance_0_2']),
                int(form.cleaned_data['ts_Alcohol_intake_frequency_Instance_0_6']),
                int(form.cleaned_data['ts_Current_tobacco_smoking_Instance_0_2']),
                
                # Float fields
                form.cleaned_data['metabolomics_Apolipoprotein_B'],
                form.cleaned_data['metabolomics_Triglycerides_in_HDL'],
                form.cleaned_data['metabolomics_Triglycerides_in_Small_HDL'],
                form.cleaned_data['metabolomics_Phospholipids_in_Very_Large_HDL'],
                form.cleaned_data['metabolomics_Omega_6_Fatty_Acids'],
                form.cleaned_data['metabolomics_Polyunsaturated_Fatty_Acids'],
                form.cleaned_data['metabolomics_Triglycerides_in_LDL'],
                form.cleaned_data['metabolomics_Free_Cholesterol_in_Large_HDL'],
                form.cleaned_data['metabolomics_Total_Lipids_in_Very_Large_HDL'],
                form.cleaned_data['metabolomics_Clinical_LDL_Cholesterol'],
            ]

            # Predict 10-year survival probability
            prob = predict_survival(input_data, model, time_horizon_days=10)
            result = prob * 100 # Convert to percentage

    else:
        form = PredictionForm()

    return render(request, 'homePage/predict.html', {'form': form, 'result': result})
