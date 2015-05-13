from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):


    class Meta:
        model = Post
        exclude = ('usuario',) # excluyo de la forma el campo 'usuario', solo recibo el texto de la publicacion
