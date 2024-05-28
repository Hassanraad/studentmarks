from django import forms

class registerForm(forms.Form):
    name = forms.CharField(max_length=20)
    universityID= forms.IntegerField()
    department= forms.CharField(max_length=20)
    stage = forms.IntegerField()