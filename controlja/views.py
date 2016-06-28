from django.http import HttpResponseRedirect,  HttpResponse
from django.core.urlresolvers import reverse
from .models import Rutas, TipoRuta,  Comentario
"""Esto es parte de lo serio"""
from django.shortcuts import render
from django.views import generic
from .forms import NewRuta
from django.template import loader

class IndexView(generic.ListView):
    template_name = 'controlja/index.html'
    context_object_name = 'latest_rutas_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Rutas.objects.order_by('-create_on')[:5]
        
class DetailView(generic.DetailView):
    model = Rutas
    template_name = 'controlja/detail.html'
    
def new_ruta(request):
    if request.method == 'POST':
        form = NewRuta(request.POST,  request.FILES)
        if form.is_valid():
            entrada = form.save()
            entrada.save()
            return HttpResponseRedirect('/')
    else:
        form = NewRuta()
        
    template = loader.get_template('controlja/new.html')
    context = {
        'form' : form
    }
    
    return HttpResponse(template.render(context,  request))
