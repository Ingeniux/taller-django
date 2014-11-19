from django.conf.urls import patterns, url
from . import views


urlpatterns = (
	url(r'^(?P<post_id>\d+)$', views.index, name="index"),
	url(r'^savepost', views.guardar_post, name="savepost"),
	)
