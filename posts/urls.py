from django.conf.urls import patterns, url
from . import views


urlpatterns = (
	url(r'^(?P<post_id>\d+)$', views.index, name="index"),
	)