from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *


from posts.forms import PostForm
def guardar_post(request):

	if request.POST:

		form = PostForm(request.POST)

		if form.is_valid:

			post = form.save(commit = False) #todavia no guardes la publicacion! me falta un dato . .
			post.usuario = request.user # le damos a la publicacion el id del usuario actual (FK)
			post.save() # ahora si guardo la publicacion

			return HttpResponseRedirect(reverse('web:index'))
	else:
		return HttpResponseRedirect(reverse('web:index'))
