from django.shortcuts import render
from .forms import PredictionForm
from .irisModel import predict

def predict_view(request):
    result = None  # Default value for result
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract features from the form
            feature1 = form.cleaned_data['sepal_length']
            feature2 = form.cleaned_data['sepal_width']
            feature3 = form.cleaned_data['petal_length']
            feature4 = form.cleaned_data['petal_width']

            
            # Create input array for the model
            input_data = [feature1, feature2, feature3, feature4]
            
            # Make prediction
            result = predict(input_data)[0]  # Assuming model returns an array
            
    else:
        form = PredictionForm()
    
    return render(request, 'homePage/predict.html', {'form': form, 'result': result})
