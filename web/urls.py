from django.conf.urls import patterns, url
from . import views


urlpatterns = (
	url(r'^$', views.index, name="index"),
	url(r'^success$', views.success, name="success"),
	)