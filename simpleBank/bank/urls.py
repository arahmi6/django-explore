from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('input_customer/', views.input_customer, name='input_customer'),
    path('input_transaction/', views.input_transaction, name='input_transaction'),
    path('point_nasabah/', views.point_nasabah, name='point_nasabah'),
    path('report_nasabah/', views.report_nasabah, name='report_nasabah'),
    # Tambahkan URL untuk menu-menu lainnya di sini
]
