#from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return render(request, 'home.html')

#def hello_world(request):
#    return HttpResponse('Hello World')
