from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_list),
    path('<int:pk>/', views.shop_detail),
    path('items/', views.item_list),
    path('items/<int:pk>/', views.item_detail),
]
