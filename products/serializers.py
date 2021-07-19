from rest_framework import serializers
from products.models import *

class AcheteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acheteur
        fields = '__all__'

class VendeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendeur
        fields = '__all__'

class ProdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdImage
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class CommandeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandeLine
        fields = '__all__'

class PanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraison
        fields = '__all__'