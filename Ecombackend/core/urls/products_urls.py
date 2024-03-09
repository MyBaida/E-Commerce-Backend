from django.urls import path
from core.views.product_views import *

urlpatterns = [

    path('', getProducts, name='products'),
    path('<str:pk>/', getProduct, name='products'),

]
