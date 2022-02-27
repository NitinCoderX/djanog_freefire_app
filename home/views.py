from django.shortcuts import render
from home.models import Video,Contact


# Create your views here.
def render_home(request):
    login_is = False
    user = request.user
    print(user)
    print(type(user))
    if user.username != "":
        login_is = True
    video  = Video.objects.all()
    context = {
        "video":video,
        "login_is":login_is,
        "user":user
    }
    return render(request,"home/home.html",context)



def render_contact(request):
    if request.method == "POST":
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        context_obj = Contact.objects.create(email=email,subject=subject,message=message)
        context_obj.save()
        login_is = False
    user = request.user
    if user.username != "":
        login_is = True
    context = {
        "login_is":login_is,
        "user":user
    }
    return render(request,"home/contact.html",context)

