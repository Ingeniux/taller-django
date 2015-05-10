from django.conf.urls import patterns, url
from . import views


urlpatterns = (
	url(r'^login', views.login_u, name="login"),
	url(r'^logout', views.logout_u, name="logout"),
	url(r'^registro', views.registro_u, name="registro"),
	)