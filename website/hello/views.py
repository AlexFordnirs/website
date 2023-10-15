from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.


def index(request):
    html = """<html><body><h1>Добро пожаловать</h1><title>Учим django</title><a href="/hello/about">О нас</a></body></html>"""
    return HttpResponse(html)

def about(request):
    html = """<html><body><title>О нас</title><a href="/hello">Главная</a></body></html>"""
    return HttpResponse(html)