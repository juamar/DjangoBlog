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
from django.core.paginator import Paginator

def indexView(request):
    idRuta = Rutas.objects.order_by('-create_on')
    paginator = Paginator(idRuta, 3)
    page = int(request.GET.get('page','1'))
    idRuta = paginator.page(page)
    tipoRuta = TipoRuta.objects.all()
    d = dict(rutas_list=idRuta, tipoRuta=tipoRuta)
    d.update(csrf(request))
    return render_to_response('controlja/index.html', d)
        
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
    return render_to_response("controlja/index.html",  {
        "results" : results, 
        "query" : query
    })
    
class FileViewSet(ModelViewSet):
    queryset= File.objects.all()
    serializer_class = FileSerializer

def ruta_filter(request, pk):
  filteredContent = Rutas.objects.filter(tipo_ruta = pk)
  tipoRuta = TipoRuta.objects.all()
  tipoRutaName = TipoRuta.objects.get(pk = pk)
  
  context = {
    
    "filteredContent" : filteredContent,
    "tipoRuta" : tipoRuta,
    "tipoRutaName" : tipoRutaName
    
  }
  return render(request, 'controlja/index.html', context)
  
def like(request, r, pk):
    like = Comentario.objects.get(pk=pk)
    like.likes += 1
    like.save()
    return HttpResponseRedirect(reverse("controlja:detail", args = (r, )))



















