from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    subtitle = models.CharField(verbose_name="Subtítulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)
    
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"] 

    def __str__(self):
        return self.title
