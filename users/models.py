from django.db import models

# Create your models here.
class Usuarios(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(default='default@example.com')
    password = models.CharField(max_length=8)
    