
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

import network.views as network_views

urlpatterns = [
	url(r'^$', network_views.home, name='home'),
	url(r'^user_page/$', network_views.user_page, name='user_page'),
	url(r'^admin/', admin.site.urls),
	url(r'^accounts/', include('registration.backends.default.urls')),
	# url(r'^test/$', network_views.test, name='test'),
	url(r'^tags-autocomplete/$', network_views.PersonalHashtagAutocomplete.as_view(), 
		name='PersonalHashtag-autocomplete'),
]
