from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return HttpResponse("heelow this is blog index")
