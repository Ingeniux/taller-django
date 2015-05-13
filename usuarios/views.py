from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
#sfrom django.core.context_processors import csrfs_token
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User




from usuarios.forms import UserForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class Registro_User(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'Nosuccess.html'
    success_url = reverse_lazy('web:index')
    #success_url = reverse('web:success')

"""
    def dispatch(self, request, *args, **kwargs):
        print args
        print kwargs
        #kwargs = {""}
        print request.user
        messages.success(request,"usuario creado")
        messages.add_message(request, messages.INFO, 'Hello world.')

        return super(Registro_User, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print "valid"
        messages.info(
            self.request,
            "Tienes un mensaje"
            )
        return super(Registro_User, self).form_valid(form)
"""       

"""
from django.shortcuts import render

def registro_u(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('web:index'))
        else:
            return render(request, "Nosuccess.html", context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('web:index'))
"""


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
def login_u(request):
    
    if  request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
    
        if form.is_valid():
    
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=usuario, password=password)
    
            if user is not None and user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('web:index'))
    
            else:
                return HttpResponse('Algo salio mal, el usuario no existe o no esta activo')
        else:
            return HttpResponse('El formulario no es valido')
    else:
        return HttpResponseRedirect(reverse('web:index'))


from django.contrib.auth.decorators import login_required
#@login_required(login_url='/user/login/')
def logout_u(request):
    logout(request)
    return HttpResponseRedirect(reverse('web:index'))
