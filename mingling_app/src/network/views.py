from django.shortcuts import render

from .forms import MinglerForm

from .models import Mingler

from django.conf import settings

import os


def home(request):
	title = 'Welcome'
	img_paths = [x[0] for x in Mingler.objects.values_list('img_path')]
	context = {
		"title": title,
		"img_paths": img_paths,
	}
	return render(request, 'home.html', context)

def user_page(request):
	title = 'Mingler Description'
	if request.POST and request.FILES:
		form = MinglerForm(request.POST, request.FILES or None)
	else:
		form = MinglerForm()
	count = Mingler.objects.filter(full_name=request.user).values_list('img_path')
	context = {
		"title": title,
		"form": form,
	}
	print('Hello')
	print(count)
	if form.is_valid():
		title = "Thank you!"
		instance = form.save(commit=False)
		instance.full_name = form.cleaned_data.get("full_name", '')
		instance.img_path = form.cleaned_data.get("img_path", '')
		print(instance.img_path)
		instance.my_hashtags = form.cleaned_data.get("my_hashtags" ,'')
		instance.looking_for_hashtags = form.cleaned_data.get("looking_for_hashtags", '')
		instance.description = form.cleaned_data.get("description", '')
		instance.save()
		context = {
			"title": title,
		}

	return render(request, 'user_page.html', context)



