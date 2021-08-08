from products import views
from django.urls.conf import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.getBest),

    path('categories/', views.ManageCategoryA.as_view()),
    path('categories/<str:slug>', views.ManageCategoryB.as_view()),

    path('products/', views.ManageProductA.as_view()),
    path('products/<int:pk>', views.ManageProductB.as_view()),
    
    path('commandes/', views.ManageCommandeA.as_view()),
    path('commandes/<int:pk>', views.ManageCommandeB.as_view()),

    path('acheteurs/', views.ManageAcheteurA.as_view()),
    path('acheteurs/<int:pk', views.ManageAcheteurB.as_view()),

    path('vendeurs/', views.ManageVendeurA.as_view()),
    path('vendeurs/<int:pk>', views.ManageVendeurB.as_view()),

    path('prodimages/', views.ManageProdImageA.as_view()),
    path('prodimages/<int:pk>', views.ManageProdImageB.as_view()),

    path('commandelines/', views.ManageCommandeLineA.as_view()),
    path('commandelines/<int:pk>', views.ManageCommandeLineB.as_view()),

    path('paniers/', views.ManagePanierA.as_view()),
    path('paniers/<int:pk>', views.ManagePanierB.as_view()),

    path('favorites/', views.ManageFavoriteA.as_view()),
    path('favorites/<int:pk>', views.ManageFavoriteB.as_view()),

    path('comments/', views.ManageCommentA.as_view()),
    path('comments/<int:pk>', views.ManageCommentB.as_view()),

    path('livraisons/', views.ManageLivraisonA.as_view()),
    path('livraisons/<int:pk>', views.ManageLivraisonB.as_view()),

    path('api-auth-token', obtain_auth_token)
]
