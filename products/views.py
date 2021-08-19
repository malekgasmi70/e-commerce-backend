from django.http.response import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from products.serializers import *
from products.models import Product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated 
# Create your views here.


class show(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ManageCategoryA(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )
    authentication_classes = [TokenAuthentication]


class ManageCategoryB(APIView):
    def get_object(self, slug):
        try:
            return Category.objects.get(slug = slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, slug):
        category = self.get_object(slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, slug):
        category = self.get_object(slug)
        serializer = CategorySerializer(category, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, slug):
        category = self.get_object(slug)
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageProductA(APIView):
    def get(self, request):
        products = Product.objects.all()
        for i in range(len(products)):
            products[i].remisePrice = products[i].remiseCal()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageProductB(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist: 
            raise Http404
    
    def get(self,request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageCommandeA(APIView):
    def get(self, request):
        commandes = Commande.objects.all()
        serializer = CommandeSerializer(commandes, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommandeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageCommandeB(APIView):
    def get_object(self, pk):
        try:
            return Commande.objects.get(pk = pk)
        except Commande.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        commande = self.get_object(pk)
        serializer = CommandeSerializer(commande)
        return Response(serializer.data)

    def put(self, request, pk):
        commande = self.get_object(pk)
        serializer = CommandeSerializer(commande, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        commande = self.get_object(pk)
        commande.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageAcheteurA(APIView):
    def get(self, request):
        acheteurs = Acheteur.objects.all()
        serializer = AcheteurSerializer(acheteurs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AcheteurSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageAcheteurB(APIView):
    def get_object(self, pk):
        try:
            return Acheteur.objects.get(pk=pk)
        except Acheteur.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        acheteur = self.get_object(pk)
        serializer = AcheteurSerializer(acheteur)
        return Response(serializer.data)

    def put(self, request, pk):
        acheteur = self.get_object(pk)
        serializer = AcheteurSerializer(acheteur, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        acheteur = self.get_object(pk)
        acheteur.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageVendeurA(APIView):
    def get(self, request):
        vendeurs = Vendeur.objects.all()
        serializer = VendeurSerializer(vendeurs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = VendeurSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageVendeurB(APIView):
    def get_object(self, pk):
        try:
            return Vendeur.objects.get(pk=pk)
        except Vendeur.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        vendeur = self.get_object(pk)
        serializer = VendeurSerializer(vendeur)
        return Response(serializer.data)

    def put(self, request, pk):
        vendeur = self.get_object(pk)
        serializer = VendeurSerializer(vendeur, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        vendeur = self.get_object(pk)
        Vendeur.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageProdImageA(APIView):
    def get(self, request):
        prodImages = ProdImage.objects.all()
        serializer = ProdImageSerializer(prodImages, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProdImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageProdImageB(APIView):
    def get_object(self, pk):
        try:
            return ProdImage.objects.get(pk=pk)
        except ProdImage.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        prodImage = self.get_object(pk)
        serializer = ProdImageSerializer(prodImage)
        return Response(serializer.data)

    def put(self, request, pk):
        prodImage = self.get_object(pk)
        serializer = ProdImageSerializer(prodImage, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        prodImage = self.get_object(pk)
        prodImage.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageCommandeLineA(APIView):
    def get(self, request):
        commandeLines = CommandeLine.objects.all()
        serializer = CommandeLineSerializer(commandeLines, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommandeLineSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageCommandeLineB(APIView):
    def get_object(self, pk):
        try:
            return CommandeLine.objects.get(pk=pk)
        except CommandeLine.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        commandeLine = self.get_object(pk)
        serializer = CommandeLineSerializer(commandeLine)
        return Response(serializer.data)

    def put(self, request, pk):
        commandeLine = self.get_object(pk)
        serializer = CommandeLineSerializer(commandeLine, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        commandeLine = self.get_object(pk)
        commandeLine.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManagePanierA(APIView):
    def get(self, request):
        paniers = Panier.objects.all()
        serializer = PanierSerializer(paniers, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PanierSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManagePanierB(APIView):
    def get_object(self, pk):
        try:
            return Panier.objects.get(pk=pk)
        except Panier.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        panier = self.get_object(pk)
        serializer = PanierSerializer(panier)
        return Response(serializer.data)

    def put(self, request, pk):
        panier = self.get_object(pk)
        serializer = PanierSerializer(panier, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        panier = self.get_object(pk)
        panier.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageFavoriteA(APIView):
    def get(self, request):
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FavoriteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageFavoriteB(APIView):
    def get_object(self, pk):
        try:
            return Favorite.objects.get(pk=pk)
        except Favorite.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        favorite = self.get_object(pk)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

    def put(self, request, pk):
        favorite = self.get_object(pk)
        serializer = FavoriteSerializer(favorite, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        favorite = self.get_object(pk)
        favorite.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageCommentA(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageCommentB(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class ManageLivraisonA(APIView):
    def get(self, request):
        livraisons = Livraison.objects.all()
        serializer = LivraisonSerializer(livraisons, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LivraisonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST
        )

class ManageLivraisonB(APIView):
    def get_object(self, pk):
        try:
            return Livraison.objects.get(pk=pk)
        except Livraison.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        livraison = self.get_object(pk)
        serializer = LivraisonSerializer(livraison)
        return Response(serializer.data)

    def put(self, request, pk):
        livraison = self.get_object(pk)
        serializer = LivraisonSerializer(livraison, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        livraison = self.get_object(pk)
        livraison.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getBest(request):
    if request.method == 'GET':
        best_sells = Product.objects.filter(best_sell = True)
        serializer = ProductSerializer(best_sells, many = True)
        return Response(serializer.data)


#class getCat(generics.ListeCreateAPIView):
    #queryset = Category.objects.all()
    #serializer_class = CategorySerializer