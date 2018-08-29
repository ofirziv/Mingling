from django import forms
from .models import Mingler, PersonalHashtag
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.forms import UserCreationForm
from dal import autocomplete
from .choices import TAGS_CHOICES


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

def get_choice_list():
    # all cites to used as chice list
    return ['Pune', 'Patna', 'Mumbai', 'Delhi']

# class PersonalHashtagForm(forms.ModelForm):
# 	# tag = forms.ModelChoiceField(queryset=PersonalHashtag.objects.all(), widget=autocomplete.ModelSelect2(url='PersonalHashtag-autocomplete'))
# 	tag = autocomplete.Select2ListChoiceField(
#         choice_list=get_choice_list,
#         widget=autocomplete.ListSelect2(url='PersonalHashtag-autocomplete')
#     )


# 	class Meta:
# 		model = PersonalHashtag
# 		fields = ('__all__')

class MinglerForm(forms.ModelForm):
	# full_name = forms.CharField(required=True)
	# my_hashtags = forms.CharField(required=False)
	# looking_for_hashtags = forms.CharField(required=False)
	description = forms.CharField(required=False, widget=forms.Textarea)
	# my_hashtags = forms.ModelChoiceField(
 	#        queryset=PersonalHashtag.objects.all(),
 	#        widget=autocomplete.ModelSelect2(url='PersonalHashtag-autocomplete'))
	personal_hashtag = forms.ModelChoiceField(
		queryset=PersonalHashtag.objects.all(),
		widget=autocomplete.ModelSelect2(url='PersonalHashtag-autocomplete'))
	looking_hashtag = forms.ModelChoiceField(
		queryset=PersonalHashtag.objects.all(),
        widget=autocomplete.ModelSelect2(url='PersonalHashtag-autocomplete'))

	class Meta:
		model = Mingler
		# fields = ['full_name', 'img_path', 'description', 'my_hashtags', 'looking_for_hashtags']
		fields = ['full_name', 'img_path', 'description']
		# widgets = {
  #           'my_hashtags': autocomplete.ListSelect2(url='PersonalHashtag-autocomplete')
  #       }


	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	return full_name














