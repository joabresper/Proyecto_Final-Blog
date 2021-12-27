'''Clase Posts'''

from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from apps.category.models import Category
from apps.user.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField('Titulo', max_length=200)
    image = models.ImageField(upload_to='media/posts_photos/%Y/%m', null=True, blank=True)
    content = models.TextField('Contenido',)
    allow_comments = models.BooleanField('Permitir comentarios', default=True)
    published_date = models.DateTimeField('Fecha de publicacion', default=timezone.now)

    category = models.ForeignKey(Category, on_delete=PROTECT, verbose_name='Categoria')        
    author = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Autor')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'