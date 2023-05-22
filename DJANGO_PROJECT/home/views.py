from django.shortcuts import render
from django.db import models

def home(request):
    return render(request, 'home.html')

def sayHello(request):
    person = {'name':'Hosein'}
    return render(request, 'hello.html', context=person)


