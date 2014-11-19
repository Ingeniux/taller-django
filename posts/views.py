from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *

def index(request, post_id):
	post = Post.objects.get(pk=post_id)
	argumentos = {"post": post}
	return render_to_response('post.html', argumentos, context_instance=RequestContext(request))


from posts.forms import PostForm
def guardar_post(request):

	if request.POST:
		form = PostForm(request.POST)
		if form.is_valid:
			usuario = request.user
			form.usuario = request.user
			form.save(instance=usuario)
			return HttpResponseRedirect(reverse('web:index'))
	else:
		return HttpResponseRedirect(reverse('web:index'))
