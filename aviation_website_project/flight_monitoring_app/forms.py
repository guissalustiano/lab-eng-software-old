from django import forms

class LoginForm(forms.Form):
	login = forms.EmailField(label='login')
	password = forms.CharField(label='password', widget=forms.PasswordInput)

class RouteSearchForm(forms.Form):
	name = forms.CharField(label='name', widget=forms.PasswordInput)