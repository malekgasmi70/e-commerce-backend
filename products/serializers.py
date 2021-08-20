from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AcheteurSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only=True)
    class Meta:
        model = Acheteur
        fields = '__all__'

class VendeurSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only = True)
    class Meta:
        model = Vendeur
        fields = '__all__'

class RegistrationVendeurSerializer(serializers.ModelSerializer):
    #password2 = serializers.CharField(style={'input_type' : 'password'}, read_only = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'isVendeur']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            isVendeur = self.validated_data['isVendeur']
        )
        password = self.validated_data['password']
        #password2 = self.validated_data['password2']

        #if password != password2:
        #    raise serializers.validatorError({'password' : 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class ProdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    vendeur = VendeurSerializer(many = False, read_only = True)
    image = ProdImageSerializer(many = True, read_only = True)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = True, read_only=True)
    class Meta:
        model = Category
        fields = ['name', 'slug', 'product']

class CommandeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = True, read_only = True)
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