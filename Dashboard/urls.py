from django.urls import path
from Dashboard import views

urlpatterns = [
    path('', views.dash, name='Dashboard'),
    path('add/<id>/', views.add, name='Add'),
    path('rm/<id>/', views.remove, name='Remove'),
]
