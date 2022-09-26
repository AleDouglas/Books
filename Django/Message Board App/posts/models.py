from django.db import models

# Create your models here.


class Post(models.Model):
    USUARIO = 'USR'
    ADMIN = 'ADM'
    AUTORES = (
        (USUARIO, 'Usuario'),
        (ADMIN, 'Administrador')
    )
    title = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 3, choices=AUTORES, default=USUARIO)
    text = models.TextField()


    def __str__(self):
        return self.title