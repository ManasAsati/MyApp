from django import forms

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    roll_number = forms.IntegerField(help_text = "Enter 8 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)