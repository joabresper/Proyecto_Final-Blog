from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.db import models
from apps.user.models import User
from apps.post.models import Post

class Comment(models.Model):
    message = models.TextField('Mensaje',)
    date = models.DateTimeField('Fecha de publicacion', default=timezone.now)

    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Usuario')
    post = models.ForeignKey(Post, on_delete=CASCADE, verbose_name='Post')

    def __str__(self):
        return User.username

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'