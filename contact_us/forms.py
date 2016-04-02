from django import forms

class contact_form(forms.Form):
    name = forms.CharField(max_length = 120, label = "Your name")
    age = forms.DecimalField(min_value = 18, max_value = 150, label = "Age")
    email = forms.EmailField(label = "E-mail address")
    comments = forms.CharField(max_length = 500, label = "Your comments")