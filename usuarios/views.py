from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect


from django.core.context_processors import csrf

from posts.models import *

from django.core.urlresolvers import reverse

from django.contrib.auth.models import User


def index(request):
    usuario_id = request.user
    posts = Post.objects.filter(usuario=usuario_id).order_by('-fecha')
    argumentos = {'title' : usuario_id, 'posts': posts, }
    return render_to_response('usuario.html', argumentos, context_instance=RequestContext(request))


from usuarios.forms import UserForm
def registro_u(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('web:index'))
    else:
        return HttpResponseRedirect(reverse('web:index'))


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
def login_u(request):
    if  request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None and user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('web:index'))
            else:
                return HttpResponse('Algo salio mal')
        else:
            return HttpResponse('El formulario no es valido')
    else:
        return HttpResponseRedirect(reverse('core:index'))


from django.contrib.auth.decorators import login_required
#@login_required(login_url='/user/login/')
def logout_u(request):
    logout(request)
    return HttpResponseRedirect(reverse('web:index'))


def timeline_usuario(request, user_name):

    usuario = User.objects.get(username=user_name)
    print (usuario.username)
    posts = Post.objects.filter(usuario=usuario.id).order_by('-fecha')
    argumentos = {'title' : usuario.username, 'id_user': usuario.id, 'posts': posts  }
    return render_to_response('usuario.html', argumentos, context_instance=RequestContext(request))
