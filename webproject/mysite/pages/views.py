from django.shortcuts import render
from itertools import product
from unicodedata import name
from webbrowser import get
from django.shortcuts import render
    
def home(request):
    return render(request,'Home.html',)
