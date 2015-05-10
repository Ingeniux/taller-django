from django.conf.urls import patterns, url
from . import views


urlpatterns = (
	url(r'^savepost', views.guardar_post, name="savepost"),
	)
