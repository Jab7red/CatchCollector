from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('catches/', views.catches_index, name='index'),
    path('catches/<int:catch_id>/', views.catches_detail, name='detail'),
    path('catches/create/', views.CatchCreate.as_view(), name='catches_create'),
    path('catches/<int:pk>/update/', views.CatchUpdate.as_view(), name='catches_update'),
    path('catches/<int:pk>/delete/', views.CatchDelete.as_view(), name='catches_delete'),
]