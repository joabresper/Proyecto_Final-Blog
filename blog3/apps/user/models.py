'''Clase User. Extension de AbstractUser'''
""" 
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    website = models.URLField('Sitio web del usuario', blank=True)
    photo = models.ImageField("Foto", upload_to='media/users_photos/%Y/%m', null=True, blank=True)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        '''Retorna nombre de usuario del Cliente'''
        return self.username
 """

from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from PIL import Image
from io import BytesIO

class Author(models.Model):
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    picture = models.ImageField(("Foto"), upload_to='users_photos/', null=True, blank=True)

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")
    
    def __str__(self):
       return self.user.get_full_name()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            img = Image.open(default_storage.open(self.picture.name))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.picture.name, buffer)



