from django.contrib import admin

from .models import Mingler, PersonalHashtag

# from .forms import PersonalHashtagForm

class MinglersAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'img_path', 'email', 'timestamp', 'updated']
	class Meta:
		model = Mingler

class PersonalHashtagAdmin(admin.ModelAdmin):
	# form = PersonalHashtagForm
	class Meta:
		model = PersonalHashtag

admin.site.register(Mingler, MinglersAdmin)
admin.site.register(PersonalHashtag, PersonalHashtagAdmin)
