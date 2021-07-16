from django.db import models
from users.models import Acheteur, Vendeur
# Create your models here.

class ProdImage(models.Model):
    image = models.ImageField(upload_to='photos/%y/%m/%d/')
    alt = models.CharField(max_length=100)
    def __str__(self):
        return self.alt

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    note = models.IntegerField()
    description = models.CharField(max_length=150)
    initPrice = models.DecimalField(max_digits=8, decimal_places=2)
    remisePrice = models.DecimalField(max_digits=8, decimal_places=2)
    remise = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(max_length=20)
    poids = models.DecimalField(max_digits=8, decimal_places=2)
    region = models.CharField(max_length=50)
    best_sell = models.BooleanField()
    disp_quantity = models.IntegerField()
    image = models.ForeignKey(ProdImage, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Commande(models.Model):
    etat = models.CharField(max_length=50)
    totalPrice = models.DecimalField(max_digits=8, decimal_places=2)
    totalPoids = models.DecimalField(max_digits=8, decimal_places=2)
    product = models.ManyToManyField(Product, null=True)
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.acheteur.firstname 

class CommandeLine(models.Model):
    quantity = models.PositiveIntegerField(default=None)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.product.name

class Panier(models.Model):
    product = models.ManyToManyField(Product, null=True)
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return "panier " + self.acheteur.firstname

class Favorite(models.Model):
    product = models.ManyToManyField(Product, null=True)
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return "Favorite " + self.acheteur.firstname

class Comment(models.Model):
    content = models.CharField(max_length=100, default=None)
    date = models.DateField(default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE)
    def __str__(self):
        return "Comment " + self.acheteur.firstname

class Livraison(models.Model):
    type = models.CharField(max_length=50, default=None)
    date_commande = models.DateField(default=None)
    date_Liv = models.DateField(default=None)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, default=None)
    acheteur = models.ForeignKey(Acheteur, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return "livraison " + self.acheteur.firstname