from django.urls import path
from myapp import views

urlpatterns = [
    path('buku/', views.buku, name='buku'),
]