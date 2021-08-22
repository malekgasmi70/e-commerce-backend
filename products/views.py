from django.http.response import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from products.serializers import *
from products.models import Product
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

########################################### Category ##############################################
@api_view(['GET'])
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser, ])
def post_category(request):
    if request.method == 'POST':
        serializer = CategoryWSerializer(data = request.data)
        
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

@api_view(['GET'])
def get_category(request, slug):
    if request.method == 'GET':
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
        serializer = CategorySerializer(category)
        return Response(serializer.data)
        
@api_view(['PUT'])
@permission_classes([IsAdminUser, ])
def put_category(request, slug):
    if request.method == 'PUT':
        user = request.user
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
        serializer = CategorySerializer(category, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
@permission_classes([IsAdminUser, ])
def delete_category(request, slug):
    if request.method == 'DELETE':
        try: 
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)    
        
##################################################### Product ####################################

@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        for i in range(len(products)):
            products[i].remisePrice = products[i].remiseCal()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_product(request):
    if request.method == 'POST':
        serializer = ProductWSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_product(request, slug):
    if request.method == 'GET':
        try:
            product = Product.objects.get(slug = slug)
        except Product.DoesNotExist:
            raise Http404
        Serializer = ProductSerializer(product)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_product(request, slug):
    if request.method == 'PUT':
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404
        user = request.user
        if product.vendeur.user != user:
            return Response({"response" : "You don't have permission to edit that. "})
        serializer = ProductWSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_product(request, slug):
    if request.method == 'DELETE':
        try:
            product = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404
        user = request.user
        if product.vendeur.user != user:
            return Response({"response" : "You don't have permission to edit that. "})
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)    

############################################################## Commande ###########################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_commandes(request):
    if request.method == 'GET':
        commandes = Commande.objects.all()
        user = request.user
        specialCommandes = {}
        for commande in commandes:
            if commande.acheteur.user == user:
                specialCommandes.append(commande)

        serializer = CommandeSerializer(specialCommandes, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_commande(request):
    if request.method == 'POST':
        serializer = CommandeWSerializer(data = request.data)
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

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_commande(request, pk):
    if request.method == 'GET':
        try:
            commande = Commande.objects.get(pk=pk)
        except Commande.DoesNotExist:
            raise Http404
        serializer = CommandeSerializer(commande)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_commande(request, pk):
    if request.method == 'PUT':
        try:
            commande = Commande.objects.get(pk=pk)
        except Commande.DoesNotExist:
            raise Http404
        serializer = CommandeWSerializer(commande, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_commande(request, pk):
    if request.method == 'DELETE':
        try: 
            commande = Commande.objects.get(pk=pk)
        except Commande.DoesNotExist:
            raise Http404
        commande.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
######################################################### Acheteur ################################

@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def get_acheteurs(request):
    if request.method == 'GET':
        acheteurs = Acheteur.objects.all()
        serializer = AcheteurSerializer(acheteurs, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser, ])
def post_acheteur(request):
    if request.method == 'POST':
        serializer = AcheteurWSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def get_acheteur(request, username):
    if request.method == 'GET':
        try:
            acheteur = Acheteur.objects.get(username=username)
        except Acheteur.DoesNotExist:
            raise Http404
        Serializer = AcheteurSerializer(acheteur)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser, ])
def put_acheteur(request, username):
    if request.method == 'PUT':
        try:
            acheteur = Acheteur.objects.get(username=username)
        except Acheteur.DoesNotExist:
            raise Http404
        serializer = AcheteurWSerializer(acheteur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser, ])
def delete_acheteur(request, username):
    if request.method == 'DELETE':
        try:
            acheteur = Acheteur.objects.get(username=username)
        except Acheteur.DoesNotExist:
            raise Http404
        acheteur.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  

########################################################### Vendeur ##############################

@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def get_vendeurs(request):
    if request.method == 'GET':
        vendeurs = Vendeur.objects.all()
        serializer = VendeurSerializer(vendeurs, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser, ])
def post_vendeur(request):
    if request.method == 'POST':
        serializer = VendeurWSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser, ])
def get_vendeur(request, username):
    if request.method == 'GET':
        try:
            vendeur = Vendeur.objects.get(username=username)
        except Vendeur.DoesNotExist:
            raise Http404
        Serializer = VendeurSerializer(vendeur)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser, ])
def put_vendeur(request, username):
    if request.method == 'PUT':
        try:
            vendeur = Vendeur.objects.get(username=username)
        except Vendeur.DoesNotExist:
            raise Http404
        serializer = VendeurWSerializer(vendeur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser, ])
def delete_vendeur(request, username):
    if request.method == 'DELETE':
        try:
            vendeur = Vendeur.objects.get(username=username)
        except Vendeur.DoesNotExist:
            raise Http404
        vendeur.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  

##################################################### ProdImage ####################################

@api_view(['GET'])
def get_prodImages(request):
    if request.method == 'GET':
        prodImages = ProdImage.objects.all()
        serializer = ProdImageSerializer(prodImages, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_prodImage(request):
    if request.method == 'POST':
        serializer = ProdImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_prodImage(request, pk):
    if request.method == 'GET':
        try:
            prodImage = ProdImage.objects.get(pk=pk)
        except ProdImage.DoesNotExist:
            raise Http404
        Serializer = ProdImageSerializer(prodImage)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_prodImage(request, pk):
    if request.method == 'PUT':
        try:
            prodImage = ProdImage.objects.get(pk=pk)
        except ProdImage.DoesNotExist:
            raise Http404
        serializer = ProdImageSerializer(prodImage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_prodImage(request, pk):
    if request.method == 'DELETE':
        try:
            prodImage = ProdImage.objects.get(pk=pk)
        except ProdImage.DoesNotExist:
            raise Http404
        prodImage.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  

################################################### CommandeLine ######################################

@api_view(['GET'])
def get_commandeLines(request):
    if request.method == 'GET':
        commandeLines = CommandeLine.objects.all()
        serializer = CommandeLineSerializer(commandeLines, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_commandeLine(request):
    if request.method == 'POST':
        serializer = CommandeLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_commandeLine(request, pk):
    if request.method == 'GET':
        try:
            commandeLine = CommandeLine.objects.get(pk=pk)
        except CommandeLine.DoesNotExist:
            raise Http404
        Serializer = CommandeLineSerializer(commandeLine)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_commandeLine(request, pk):
    if request.method == 'PUT':
        try:
            commandeLine = CommandeLine.objects.get(pk=pk)
        except CommandeLine.DoesNotExist:
            raise Http404
        serializer = CommandeLineSerializer(commandeLine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_commandeLine(request, pk):
    if request.method == 'DELETE':
        try:
            commandeLine = CommandeLine.objects.get(pk=pk)
        except CommandeLine.DoesNotExist:
            raise Http404
        commandeLine.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  

############################################### Panier ##########################################

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_paniers(request):
    if request.method == 'GET':
        paniers = Panier.objects.all()
        serializer = PanierSerializer(paniers, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_panier(request):
    if request.method == 'POST':
        serializer = PanierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_panier(request, pk):
    if request.method == 'GET':
        try:
            panier = Panier.objects.get(pk=pk)
        except Panier.DoesNotExist:
            raise Http404
        Serializer = PanierSerializer(panier)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_panier(request, pk):
    if request.method == 'PUT':
        try:
            panier = Panier.objects.get(pk=pk)
        except Panier.DoesNotExist:
            raise Http404
        serializer = PanierSerializer(panier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_panier(request, pk):
    if request.method == 'DELETE':
        try:
            panier = Panier.objects.get(pk=pk)
        except Panier.DoesNotExist:
            raise Http404
        panier.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)  

############################################### Favorite ##########################################

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_favorites(request):
    if request.method == 'GET':
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(favorites, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_favorite(request):
    if request.method == 'POST':
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_favorite(request, pk):
    if request.method == 'GET':
        try:
            favorite = Favorite.objects.get(pk=pk)
        except Favorite.DoesNotExist:
            raise Http404
        Serializer = FavoriteSerializer(favorite)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_favorite(request, pk):
    if request.method == 'PUT':
        try:
            favorite = Favorite.objects.get(pk=pk)
        except Favorite.DoesNotExist:
            raise Http404
        serializer = FavoriteSerializer(favorite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_favorite(request, pk):
    if request.method == 'DELETE':
        try:
            favorite = Favorite.objects.get(pk=pk)
        except Favorite.DoesNotExist:
            raise Http404
        favorite.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 

################################################# Comment ########################################

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_comments(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_comment(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_comment(request, pk):
    if request.method == 'GET':
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        Serializer = CommentSerializer(comment)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_comment(request, pk):
    if request.method == 'PUT':
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_comment(request, pk):
    if request.method == 'DELETE':
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 

################################################ Livraison #########################################

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_livraisons(request):
    if request.method == 'GET':
        livraisons = Livraison.objects.all()
        serializer = LivraisonSerializer(livraisons, many = True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def post_livraison(request):
    if request.method == 'POST':
        serializer = LivraisonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_livraison(request, pk):
    if request.method == 'GET':
        try:
            livraison = Livraison.objects.get(pk=pk)
        except Livraison.DoesNotExist:
            raise Http404
        Serializer = LivraisonSerializer(livraison)
        return Response(Serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def put_livraison(request, pk):
    if request.method == 'PUT':
        try:
            livraison = Livraison.objects.get(pk=pk)
        except Livraison.DoesNotExist:
            raise Http404
        serializer = LivraisonSerializer(livraison, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ])
def delete_livraison(request, pk):
    if request.method == 'DELETE':
        try:
            livraison = Livraison.objects.get(pk=pk)
        except Livraison.DoesNotExist:
            raise Http404
        livraison.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 

################################################ BestSells #########################################

@api_view(['GET'])
def getBest(request):
    if request.method == 'GET':
        best_sells = Product.objects.filter(best_sell = True)
        serializer = ProductSerializer(best_sells, many = True)
        return Response(serializer.data)

############################################### Registration ##########################################

@api_view(['POST',])
def registration_vendeur_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = " successfully registred a new user."
            data['email'] = user.email
            data['username'] = user.username
            data['isVendeur'] = user.isVendeur
            data['isAcheteur'] = user.isAcheteur
            token = Token.objects.get(user=user).key
            data['token']= token
            if user.isVendeur == True:
                vendeur = Vendeur(user=user)
                vendeur.save()
            elif user.isAcheteur == True:
                acheteur = Acheteur(user = user)
                acheteur.save()
        else:
            data = serializer.errors
        return Response(data)   
    
################################################# End. ########################################