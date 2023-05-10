from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/<int:pk>/', views.download_file, name='download_file'),
]
