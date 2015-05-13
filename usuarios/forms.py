from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserForm(ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'contrasena'}))


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']



	def save(self, commit=True):
    	# Save the provided password in hashed format
		user = super(forms.ModelForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user

