from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def pas(request):
    thepassword = ''
    caratcers = 'abcdef'
    length = int(request.GET.get('length'))

    if request.GET.get('numbers'):
        caratcers+='0987654321'

    if request.GET.get('spec'):
        caratcers+=')(*&^%$#@!'

    if request.GET.get('uppercase'):
        caratcers+='ABCDEFG'

    for x in range(length):
        thepassword+= random.choice(caratcers)


    return render(request, 'generator/pas.html', {'password': thepassword})
