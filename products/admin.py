from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ProdImage)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Commande)
admin.site.register(CommandeLine)
admin.site.register(Panier)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Livraison)