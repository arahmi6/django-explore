from django.urls import path
from .views import PelangganListCreateView, PelangganDetailView

urlpatterns = [
    path('pelanggan/', PelangganListCreateView.as_view(), name='pelanggan-list-create'),
    path('pelanggan/<int:pk>/', PelangganDetailView.as_view(), name='pelanggan-detail'),
]
