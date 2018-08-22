from django.contrib import admin

from .models import Mingler

class MinglersAdmin(admin.ModelAdmin):
	list_display = ["__str__", "full_name", "img_path", "timestamp", "updated"]
	class Meta:
		model = Mingler

admin.site.register(Mingler)
