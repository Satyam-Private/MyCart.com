from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
    return render(request , 'shop\index.html')


def about_Us(request):
    return HttpResponse("this is the about us page")
def contact_Us(request):
    return HttpResponse("this is contact us page")
def products(request): 
    return HttpResponse("this is the products page")
def search(request):
    return HttpResponse("this is the search page")
