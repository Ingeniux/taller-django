from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('web.urls', namespace='web')),
    url(r'^u/', include('usuarios.urls', namespace="usuarios")),
    url(r'^p/', include('posts.urls', namespace="posts")),
    url(r'^admin/', include(admin.site.urls)),
)
