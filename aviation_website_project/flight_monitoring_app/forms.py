from django import forms

class LoginForm(forms.Form):
	login = forms.EmailField(label='login')
	password = forms.CharField(label='password', widget=forms.PasswordInput)