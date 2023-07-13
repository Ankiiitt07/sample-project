from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def welcome(response):
    return HttpResponse("Hello World")

def login(request):
    return render(request, 'login.html')

def authentication(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if (email == "ankit@wethink.co.in" and password == "123456"):
            return HttpResponse("Success")
        else:
            error_email = []
            items = {
                "status" : "error",
                "message" : "Invalid Credential"
            }
            error_email.append(items)
            return render(request, 'login.html', {'error_email' : error_email})