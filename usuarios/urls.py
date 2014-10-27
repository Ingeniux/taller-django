from django.conf.urls import patterns, url
from . import views


urlpatterns = (
	url(r'^$', views.index, name="index"),
	url(r'^login', views.login_u, name="login"),
	url(r'^logout', views.logout_u, name="logout"),
	url(r'^registro', views.registro_u, name="registro"),
	url(r'^(?P<user_name>[0-9a-zA-Z_-]+)$', views.timeline_usuario, name="usuario"),
	)