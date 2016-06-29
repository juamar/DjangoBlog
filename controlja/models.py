from django.db import models
from django.conf import settings

UPLOADS_DIR = getattr(settings,  "UPLOADS_DIR",  "controlja/static/uploads")

class TipoRuta(models.Model):
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo

class Rutas(models.Model):
    titulo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    distancia = models.DecimalField(max_digits=6, decimal_places=2)
    autor = models.CharField(max_length=100)
    tipo_ruta = models.ForeignKey(TipoRuta, on_delete=models.SET_NULL,  null=True)
    altrimetria_base = models.DecimalField(max_digits=6, decimal_places=2)
    altimetria_final = models.DecimalField(max_digits=6, decimal_places=2)
    desnivel = models.DecimalField(max_digits=6, decimal_places=2)
    recorrido_circular = models.DecimalField(max_digits=6, decimal_places=2)
    recorrido_lineal = models.DecimalField(max_digits=6, decimal_places=2)
    libro_ruta = models.TextField()
    detalles = models.TextField()
    create_on = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.titulo + ", " + self.direccion
        
class Comentario(models.Model):
    ruta = models.ForeignKey(Rutas, on_delete=models.SET_NULL, null=True)
    autor = models.CharField(max_length=100)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.autor

class File(models.Model):
    file = models.FileField(upload_to=UPLOADS_DIR)
    create_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now_add = True)
    ruta = models.ForeignKey(Rutas, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.file
