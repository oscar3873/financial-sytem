from django.db import models

from adviser.models import Adviser

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name="Titulo de la nota")
    content = models.TextField(max_length=250, blank=True, null=True, verbose_name="Contenido de la nota")
    user = models.ForeignKey(Adviser, on_delete=models.DO_NOTHING, blank=True, null=True, default=None, help_text="Notas de Usuario", related_name="user_notes")
    color = models.CharField(max_length=10, blank=True, null=True, help_text="Color de la nota")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    def all_properties(self):
        return ["Titulo","Fecha de Creacion","Por"]

    class Meta:
        ordering = ["created_at"]