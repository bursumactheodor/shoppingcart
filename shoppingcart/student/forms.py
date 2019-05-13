
from django import forms

class StudentForm(forms.Form):
    #id=forms.IntegerField()
    nume = forms.CharField()
    telefon = forms.CharField()
    bursa = forms.DecimalField()
    localitate = forms.CharField()



