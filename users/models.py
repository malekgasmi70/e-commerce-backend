from django.db import models

# Create your models here.
class Acheteur(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    pays = models.CharField(max_length=30)
    codepostal= models.IntegerField(max_length=10)
    def __str__(self):
        return self.firstname


class Vendeur(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=30)
    tel = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)
    pays = models.CharField(max_length=30)
    codepostal= models.IntegerField()
    def __str__(self):
        return self.firstname


