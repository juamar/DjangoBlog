from django.conf.urls import url,  include
from .views import *
from rest_framework.routers import SimpleRouter
from .views import FileViewSet

router = SimpleRouter()
router.register(r'files',  FileViewSet)

app_name = 'controlja'
urlpatterns = [
	url(r'^$', indexView, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', detail_view, name='detail'),
    url(r'^new/',  new_ruta,  name='new'),
    url(r'newComentario/(\d+)/$',  new_comentario, name='new_comentario'), 
    url(r'search/$',  search, name='search'), 
    url(r'^',  include(router.urls)), 
    url(r'^tipo/(?P<pk>\d+)/$', ruta_filter, name='filter'),
    url(r'^like/(?P<r>\d+)/(?P<pk>\d+)/$', like, name='like'),
]
