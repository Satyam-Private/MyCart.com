from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name = 'shopindex'),
    path('about_Us' , views.about_Us , name = 'about_Us' ), 
    path('contact_Us' , views.contact_Us , name = ' contact_Us' ),
    path('products' , views.products , name = 'products' ),
    path('search' , views.search , name = 'search' )
]