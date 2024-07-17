#from django.http import HttpResponse
from django.shortcuts import render

def Home_page(request):
    #return HttpResponse("hola mundo")
    return render(request, "Home.html")

def Fiction_page(request):
    #return HttpResponse("hola about")
    return render(request, "Fiction.html")