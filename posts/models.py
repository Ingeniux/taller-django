from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField(auto_now_add=True)
	contenido = models.CharField(max_length=130)

	def __unicode__(self):
		return u'%s ' % (self.usuario)