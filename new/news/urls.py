from django.urls import path
from . import views

urlpatterns = [
    path('', views.dom, name='dom'),
]