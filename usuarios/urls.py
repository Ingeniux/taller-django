from django.conf.urls import patterns, url
from . import views
from views import Registro_User




urlpatterns = (
	url(r'^login', views.login_u, name="login"),
	url(r'^logout', views.logout_u, name="logout"),
	url(r'^registro', Registro_User.as_view(), name="registro"),
	)