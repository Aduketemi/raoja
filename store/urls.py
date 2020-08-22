from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('register/', views.registerPage, name= 'register'),
    path('login/', views.loginPage, name= 'login'),
    path('logout/', views.logoutPage, name= 'logout'),

    path('', views.store, name= 'store'),
    path('cart/', views.cart, name= 'cart'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('process_order/', views.processOrder, name= 'process_order'),
] 