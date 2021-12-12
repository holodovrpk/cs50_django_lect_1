from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.privet, name='privet'),
    path("alex", views.alex, name='alex'),
    path("bob", views.bob, name='bob')
]