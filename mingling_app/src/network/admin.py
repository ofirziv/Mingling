from django.contrib import admin

from .models import Mingler

class MinglersAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'img_path', 'email', 'timestamp', 'updated']
	class Meta:
		model = Mingler

admin.site.register(Mingler, MinglersAdmin)
