from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('get_customer_data/', views.get_customer_data, name='get_customer_data'),
    path('get_transaksi_data/', views.get_transaksi_data, name='get_transaksi_data'),
    path('get_redis_data/', views.get_redis_data, name='get_redis_data'),
    # ...
]
