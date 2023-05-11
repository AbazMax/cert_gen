from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generating_file', views.generating_file, name='generating_file'),
    path('download/<int:pk>/', views.download_file, name='download_file'),
]
