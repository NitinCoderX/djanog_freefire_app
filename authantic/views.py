from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from urllib3 import HTTPResponse
from authantic.models import Phone,PhoneUserRelationship
from django.contrib import messages
# Create your views here.

def phone_handel(request):
    if request.method == "POST":
        phone_number = request.POST["phone"]

        if phone_number.__len__() != 12:
            return redirect("auth:phone")

        
        print(Phone.objects.filter(phone_number=phone_number).exists())
        if Phone.objects.filter(phone_number=phone_number).exists() == True :
        
            print("ok")
            return redirect("auth:phone")
        else:
               
            Phone.objects.create(phone_number=phone_number)
            context = {
                    "phone":phone_number
                }
            return render(request,"authantic/signin.html",context)
    print("ok!!!")
    return render(request,"authantic/phone.html")



def signin_handle(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        conf_password = request.POST["conf-password"]
        phone = request.POST["phones"]
        print(phone)
        if password != conf_password:
            return redirect("auth:phone")

        if User.objects.filter(username=username).exists() == True:
            return redirect("auth:phone")

        User_module = User.objects.create_user(username=username,password=password)

        phone_obj = Phone.objects.get(phone_number=phone)
        PhoneUserRelationship.objects.create(phone=phone_obj,User=User_module)
        return redirect("auth:login")

    return redirect("auth:phone") 

def login_handel(request):
    if request.method == "POST":
        username= request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect("home:home")
    return render(request,"authantic/login.html")





@login_required
def logout_handel(request):
    print("ok")
    logout(request)
    return redirect("auth:login")