from django.conf.urls import url
from . import views
from .views import new_ruta,  new_comentario,  detail_view

app_name = 'controlja'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', detail_view, name='detail'),
    url(r'^new/',  new_ruta,  name='new'), 
    url(r'newComentario/(\d+)/$',  new_comentario, name='new_comentario')
]
