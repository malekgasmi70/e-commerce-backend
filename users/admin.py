from django.contrib import admin
from .models import Acheteur, Vendeur

# Register your models here.
admin.site.register(Acheteur)
admin.site.register(Vendeur)