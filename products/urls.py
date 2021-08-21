from products import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.getBest),

    path('categories/', views.get_categories),
    path('categories/create', views.post_category),
    path('categories/<str:slug>', views.get_category),
    path('categories/<str:slug>/update', views.put_category),
    path('categories/<str:slug>/delete', views.delete_category),

    path('products/', views.get_products),
    path('products/create', views.post_product),
    path('products/<str:slug>', views.get_product),
    path('products/<str:slug>/update', views.put_product),
    path('products/<str:slug>/delete', views.delete_product),
    
    path('commandes/', views.get_commandes),
    path('commandes/create', views.post_commande),
    path('commandes/<str:slug>', views.get_commande),
    path('commandes/<str:slug>/update', views.put_commande),
    path('commandes/<str:slug>/delete', views.delete_commande),

    
    path('acheteurs/', views.get_acheteurs),
    path('acheteurs/create', views.post_acheteur),
    path('acheteurs/<str:username>', views.get_acheteur),
    path('acheteurs/<str:username>/update', views.put_acheteur),
    path('acheteurs/<str:username>/delete', views.delete_acheteur),

    path('vendeurs/', views.get_vendeurs),
    path('vendeurs/create', views.post_vendeur),
    path('vendeurs/<str:username>', views.get_vendeur),
    path('vendeurs/<str:username>/update', views.put_vendeur),
    path('vendeurs/<str:username>/delete', views.delete_vendeur),

    
    path('prodImages/', views.get_prodImages),
    path('prodImages/create', views.post_prodImage),
    path('prodImages/<int:pk>', views.get_prodImage),
    path('prodImages/<int:pk>/update', views.put_prodImage),
    path('prodImages/<int:pk>/delete', views.delete_prodImage),

    
    path('commandeLines/', views.get_commandeLines),
    path('commandeLines/create', views.post_commandeLine),
    path('commandeLines/<int:pk>', views.get_commandeLine),
    path('commandeLines/<int:pk>/update', views.put_commandeLine),
    path('commandeLines/<int:pk>/delete', views.delete_commandeLine),

    
    path('paniers/', views.get_paniers),
    path('paniers/create', views.post_panier),
    path('paniers/<int:pk>', views.get_panier),
    path('paniers/<int:pk>/update', views.put_panier),
    path('paniers/<int:pk>/delete', views.delete_panier),

    
    path('favorites/', views.get_favorites),
    path('favorites/create', views.post_favorite),
    path('favorites/<int:pk>', views.get_favorite),
    path('favorites/<int:pk>/update', views.put_favorite),
    path('favorites/<int:pk>/delete', views.delete_favorite),

    
    path('comments/', views.get_comments),
    path('comments/create', views.post_comment),
    path('comments/<int:pk>', views.get_comment),
    path('comments/<int:pk>/update', views.put_comment),
    path('comments/<int:pk>/delete', views.delete_comment),

    
    path('livraisons/', views.get_livraisons),
    path('livraisons/create', views.post_livraison),
    path('livraisons/<int:pk>', views.get_livraison),
    path('livraisons/<int:pk>/update', views.put_livraison),
    path('livraisons/<int:pk>/delete', views.delete_livraison),

    path('register/', views.registration_vendeur_view),
    path('login/', obtain_auth_token)


]