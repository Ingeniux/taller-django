from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, help_text='Lo mas larga posible')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']


	def clean_password2(self):
	# verifica si los password ingresados son identicos
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self, commit=True):
    	# Almacena el password en un hash
		user = super(forms.ModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
