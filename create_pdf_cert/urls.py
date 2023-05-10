from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('download/<int:pk>/', views.download_file, name='download_file'),
]
