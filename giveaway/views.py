from django.shortcuts import render
from home.models import Video
from giveaway.models import Giveaway


# Create your views here.
def show_giveaway(request):
    login_is = False
    is_give = True
    user = request.user
    if user.username != "":
        login_is = True

    Giveaways = Giveaway.objects.all()
    if Giveaways.__len__() == 0:
        is_give = False
    context = {
        "login_is":login_is,
        "user":user,
        "Giveaway":Giveaways,
        "is_give":is_give
    }
    return render(request,"giveaway/show_give_away.html",context)