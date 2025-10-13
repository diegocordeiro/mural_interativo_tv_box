from django.shortcuts import render
from .models import Banner

def home(request):
    banners = Banner.objects.filter(ativo=True).order_by('ordem', '-criado')
    return render(request, 'mural/home.html', {'banners': banners})
