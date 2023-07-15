from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cert', views.generating_file, name='cert'),
    path('download/<int:pk>/', views.download_file, name='download_file'),
]
