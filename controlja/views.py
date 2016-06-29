from django.http import HttpResponseRedirect,  HttpResponse
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render,  render_to_response
from django.views import generic
from .forms import NewRuta,  FormularioComentario
from django.template import loader
from django.core.context_processors import csrf
from django.db.models import Q
from .serializers import FileSerializer
from rest_framework.viewsets import ModelViewSet

class IndexView(generic.ListView):
    template_name = 'controlja/index.html'
    context_object_name = 'latest_rutas_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Rutas.objects.order_by('-create_on')[:5]
        
def detail_view(request, pk):
    idRuta = Rutas.objects.get(pk=int(pk))
    d = dict(rutas=idRuta, form=FormularioComentario())
    d.update(csrf(request))
    return render_to_response('controlja/detail.html', d)
    
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
    
def new_comentario(request,  pk):
    p = request.POST
    
    if 'text' in p:
        autor = 'anonymous'
        if p['autor']:
            autor = p['autor']
            
        comentario = Comentario(ruta=Rutas.objects.get(pk=pk))
        cf = FormularioComentario(p,  instance=comentario)
        cf.fields['autor'].required = False
        cf.fields['likes'].required = False
        
        comentario = cf.save(commit=False)
        comentario.autor = autor
        comentario.likes = 0
        comentario.save()
        return HttpResponseRedirect(reverse('controlja:detail',  args = (pk, )))
        
def search(request):
    query = request.GET.get('q',  '')
    if query:
        qset = (
            Q(titulo__icontains=query) |
            Q(direccion__icontains=query) |
            Q(autor__icontains=query) |
            Q(detalles__icontains=query) |
            Q(libro_ruta__icontains=query)
        )
        results = Rutas.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("controlja/search.html",  {
        "results" : results, 
        "query" : query
    })
    
class FileViewSet(ModelViewSet):
    queryset= File.objects.all()
    serializer_class = FileSerializer





















