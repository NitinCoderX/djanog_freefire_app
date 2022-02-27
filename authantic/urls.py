from django.urls import path
from authantic.views import phone_handel,signin_handle,login_handel,logout_handel

app_name="auth"

urlpatterns = [
    path("phone/",phone_handel,name="phone"),
    path("signin/",signin_handle,name="signin"),
    path("login/",login_handel,name="login"),
    path("logout/",logout_handel,name="logout"),
]