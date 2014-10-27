from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse, HttpResponseRedirect

from .models import *

def index(request, post_id):
	post = Post.objects.get(pk=post_id)
	argumentos = {"post": post}
	return render_to_response('post.html', argumentos, context_instance=RequestContext(request))