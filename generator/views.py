from django.shortcuts import render

from django.http import HttpResponse

import random

# Create your views here.



def home(request):
    return render(request, 'generator/home.html')

def password(request):

    lch=list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('up'):
        lch.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('spc'):
        lch.extend('!@#$%^&*()_+')
    if request.GET.get('nm'):
        lch.extend('0123456789')

    len=int(request.GET.get('length',12))

    pw=''

    for x in range(len):
        pw+=random.choice(lch)

    return render(request, 'generator/password.html', {'password': pw})

def about(request):
    return render(request, 'generator/about.html')