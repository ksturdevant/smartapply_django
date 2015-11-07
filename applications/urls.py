from django.conf.urls import url, include, patterns

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^applications/', include('applications.urls', namespace="applications")),
	url(r'^(?P<application_id>[0-9]+)/$', views.detail, name='detail'),	
	]