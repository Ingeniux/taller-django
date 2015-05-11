from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from django.contrib.auth.forms import AuthenticationForm
from django.core.context_processors import csrf

from usuarios.forms import UserForm
from posts.models import *

def index(request):
	auth_form = AuthenticationForm()
	reg_form = UserForm()
	posts = Post.objects.all()#para efectos de debug como dice asly
	argumentos = {'title': 'Inicio', 'auth_form': auth_form, 'reg_form': reg_form, 'posts': posts }
	return render(request, "base.html", argumentos, context_instance=RequestContext(request))


def success (request):
	return HttpResponse("Hello, world. You're at the polls index.")
