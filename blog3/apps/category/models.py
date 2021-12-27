from django.db import models

'''Clase Categorias'''

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, unique=True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'