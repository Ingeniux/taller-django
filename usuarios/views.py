from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from posts.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User



"""
Esta funcion pienso que es mejor ponerla como clase,
para explicar lo de las vistas-form como clases, puesto que ya hay un form como funcion.
la idea es que si se crea el usuario se pueda mostrar un mensaje al usuario, o si hay error tambien.
"""
from usuarios.forms import UserForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

class Registro_User(CreateView):
    form_class = UserForm
    template_name = 'Nosuccess.html'
    success_url = reverse_lazy('web:success')

    
        
# def registro_u(request):
#     if request.POST:
#         form = UserForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return HttpResponseRedirect(reverse('web:index'))
#     else:
#         return HttpResponseRedirect(reverse('web:index'))


"""
Fin
"""

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