from django.shortcuts import render
from .models import LoginData

# Create your views here.
def login(request):
    return render(request,'pages/login.html')
def error(request):
    return render(request,'pages/error.html')
def success(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        login = LoginData.objects.create(username=username, password=password) 
        login.save() 
        # context ={
        #     'username' : username,
        #     'password' : password
        # }
        return render(request,'pages/success.html')
    return render(request,'pages/success.html')
def error_404_view(request, exception):
    return render(request,'pages/login.html')