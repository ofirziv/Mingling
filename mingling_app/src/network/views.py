from django.shortcuts import render
from .forms import MinglerForm
from .models import Mingler
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
	form = MinglerForm(request.POST or None, request.FILES or None)
	instance = Mingler.objects.get(email=request.user.email)
	# count = Mingler.objects.filter(full_name=request.user).values_list('img_path')
	context = {
		"title": title,
		"form": form,
		"email": request.user.email,
		"img_path": instance.img_path,
		"finished": "no"
	}
	# print('Hello')
	# print(count)
	# print(request.user.email)
	# print(User.objects.filter(email=request.user.email))
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
			instance.my_hashtags = form.cleaned_data.get("my_hashtags" ,'')
			instance.looking_for_hashtags = form.cleaned_data.get("looking_for_hashtags", '')
			instance.description = form.cleaned_data.get("description", '')
			instance.save()

		# context = {
		# 	"title": title,
		# 	"finished": "yes",
		# }
	return render(request, 'user_page.html', context)



