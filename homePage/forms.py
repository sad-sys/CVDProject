from django import forms

class PredictionForm(forms.Form):
    sepal_length = forms.FloatField(label='sepal_length')
    sepal_width = forms.FloatField(label='sepal_width')
    petal_length = forms.FloatField(label='petal_length')
    petal_width = forms.FloatField(label='petal_width')
