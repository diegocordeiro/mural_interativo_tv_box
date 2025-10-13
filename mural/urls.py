from django.urls import path
from . import views

app_name = 'mural'
urlpatterns = [
    path('', views.home, name='home'),
]
