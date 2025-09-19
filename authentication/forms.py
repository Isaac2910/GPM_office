from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label ='identifiant', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')
    
