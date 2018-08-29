from django.shortcuts import render
from .forms import MinglerForm
from .models import Mingler, PersonalHashtag
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dal import autocomplete


import os


def home(request):
	title = 'Welcome'
	img_paths = [x[0] for x in Mingler.objects.values_list('img_path')]
	username_list = [x[0] for x in Mingler.objects.values_list('full_name')]
	descriptions = [x[0] for x in Mingler.objects.values_list('description')]
	print(img_paths)
	context = {
		"title": title,
		"img_paths": img_paths,
		"username_list": username_list,
		"data": zip(img_paths, username_list, descriptions),
	}
	return render(request, 'home.html', context)

@login_required
def user_page(request):
	title = 'Mingler Description'
	
	try:
		instance = Mingler.objects.get(email=request.user.email)
		form = MinglerForm(request.POST or None, request.FILES or None, 
			initial={'full_name': instance.full_name, 'img_path': instance.img_path, 'my_hashtags': '',
			'looking_for_hashtags': '', 'description': instance.description})
		context = {
		"title": title,
		"form": form,
		"email": request.user.email,
		"img_path": instance.img_path,
		"finished": "no"
	}
	except:
		form = MinglerForm(request.POST or None, request.FILES or None)
		context = {
		"title": title,
		"form": form,
		"email": request.user.email,
		"finished": "no"
	}

	print(form.is_valid())
	if form.is_valid():
		print('Valid!!!')
		title = "Thank you!"
		instance = Mingler.objects.filter(email=request.user.email)
		if not instance:
			print('Creating!!!!')
			instance = form.save(commit=False)
			instance.full_name = form.cleaned_data.get("full_name", '')
			instance.img_path = form.cleaned_data.get("img_path", '')
			instance.my_hashtags = form.cleaned_data.get("my_hashtags" ,'')
			instance.looking_for_hashtags = form.cleaned_data.get("looking_for_hashtags", '')
			instance.description = form.cleaned_data.get("description", '')
			instance.email = request.user.email
			instance.save()
		else:
			instance = Mingler.objects.get(email=request.user.email)
			print('Updating!!!!')
			instance.full_name = form.cleaned_data.get("full_name", '')
			instance.img_path = form.cleaned_data.get("img_path", '')

			personal_tag = form.cleaned_data.get("personal_hashtag" ,'').tag
			personal_hashtags = instance.my_hashtags.split(',')
			if not personal_tag in personal_hashtags and personal_tag != '':
				instance.my_hashtags = '{},{}'.format(instance.my_hashtags, personal_tag)

			looking_tag = form.cleaned_data.get("looking_hashtag", '').tag
			looking_hashtags = instance.looking_for_hashtags.split(',')
			if not looking_tag in looking_hashtags and looking_tag != '':
				instance.looking_for_hashtags = '{},{}'.format(instance.looking_for_hashtags, looking_tag)

			instance.description = form.cleaned_data.get("description", '')
			print(instance.img_path)
			if instance.img_path == 'no-img.jpg':
				print('partially')
				instance.save(update_fields=["full_name", "my_hashtags", "looking_for_hashtags", "description"])
			else:
				print('full')
				instance.save()

		# context = {
		# 	"title": title,
		# 	"finished": "yes",
		# }
	return render(request, 'user_page.html', context)

class PersonalHashtagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        # if not self.request.user.is_authenticated():
        #     return PersonalHashtag.objects.none()

        qs = PersonalHashtag.objects.all()

        if self.q:
            qs = qs.filter(tag__istartswith=self.q)

        return qs

    # def get_list(self):
    #     # return all cities name here, it will be auto filtered by super class
    #     return ['Pune', 'Patna', 'Mumbai', 'Delhi'] 



















