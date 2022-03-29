# Create your views here.
from django.shortcuts import render
import re


def main_view(request):
    return render(request, 'main.html', {})


def search(request):
    return render(request, 'search.html', {})

