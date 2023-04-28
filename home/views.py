from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render (request, "home/home.html")
    #return HttpResponse("<h2>Welcome to the store!</h2><a href='/stock/all-items'>Check out our stock</a>")