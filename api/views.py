from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

# Create your views here.
def welcome(response):
    return HttpResponse("Hello World")

def login(request):
    return render(request, 'login.html')

@api_view(["POST"])
def authentication(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if (email == "ankit@wethink.co.in" and password == "123456"):
            output = {
                "status" : "Success",
                "message" : "Successfully logged In"
            }
            return JsonResponse(output, status=200)
        else:
            error_email = []
            items = {
                "status" : "error",
                "message" : "Invalid Credential"
            }
            error_email.append(items)
            return render(request, 'login.html', {'error_email' : error_email})