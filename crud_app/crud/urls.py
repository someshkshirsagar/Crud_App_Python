from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products, name="products"),
    path('add/', views.add, name="add"),
    path('add_user/', views.add_user, name='add_user'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('order/', views.order, name='order'),
    path('place_order/', views.place_order, name='place_order'),
    path('update/uprec/<int:id>/', views.uprec, name='uprec'),

    path('add_product/', views.add_product, name='add_product'),
    path('add_product_service/', views.add_product_service, name='add_product_service'),
    
]
