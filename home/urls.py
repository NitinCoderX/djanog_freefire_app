from django.urls import path
from home.views import render_home,render_contact

app_name="home"

urlpatterns = [
    path("",render_home,name="home"),
    path("contact/",render_contact,name="contact")
]
