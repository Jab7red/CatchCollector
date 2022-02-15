from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catches/', views.catches_index, name='index'),
    path('catches/<int:catch_id>/', views.catches_detail, name='detail'),
]