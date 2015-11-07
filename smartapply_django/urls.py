
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
	url(r'^applications/', include('applications.urls')),
	url(r'^admin/', include(admin.site.urls)),
	]
