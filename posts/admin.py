from django.contrib import admin

from .models import *

class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha']

admin.site.register(Post, postAdmin)
