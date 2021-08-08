from django.db import models
from django.db.models.fields.related import ForeignKey

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
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, default=None)
    vendeur = models.ForeignKey(Vendeur, related_name='vendeur', on_delete=models.CASCADE, default=None)
    image = models.ManyToManyField(ProdImage, null=True)
    

    def remiseCal(self):
        return self.initPrice - self.initPrice*self.remise

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
