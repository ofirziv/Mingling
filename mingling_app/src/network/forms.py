from django import forms

from .models import Mingler

from registration.forms import RegistrationFormUniqueEmail

from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()


# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields=['full_name', 'email']

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base, provider = email.split("@")
# 		domain, extension = provider.split('.')
# 		if not extension == "edu":
# 			raise forms.ValidationError("Please use a valid .EDU email address")
# 		return email

# 	def clean_full_name(self):
# 		full_name = self.cleaned_data.get('full_name')
# 		return full_name

class MinglerForm(forms.ModelForm):
	# full_name = forms.CharField(required=True)
	# my_hashtags = forms.CharField(required=False)
	# looking_for_hashtags = forms.CharField(required=False)
	# description = forms.CharField(required=False)

	class Meta:
		model = Mingler
		# fields = ['full_name', 'img_path', 'description', 'my_hashtags', 'looking_for_hashtags']
		fields = ['full_name', 'img_path']

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	return full_name










