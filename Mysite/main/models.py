from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Credenciais(models.Model):
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Email(models.Model):
    to = models.EmailField()
    send_date = models.DateField()
    send_time = models.TimeField()
    template = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)

class Objetos(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(Objetos, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Click(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)