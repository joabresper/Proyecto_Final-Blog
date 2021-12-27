'Modelo para Calificaciones'

from django.db import models
from django.db.models.deletion import CASCADE
from apps.user.models import User
from apps.post.models import Post


class Calification(models.Model):

    POINTS_OPTIONS = [
        (1 , '1'),
        (2 , '2'),
        (3 , '3'),
        (4 , '4'),
        (5 , '5'),
    ]

    points = models.IntegerField('Calificacion', choices=POINTS_OPTIONS)

    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Usuario')
    post = models.ForeignKey(Post, on_delete=CASCADE, verbose_name='Post')

    def __str__(self):
        return self.points