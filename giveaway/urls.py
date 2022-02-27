from django.urls import path
from giveaway.views import show_giveaway

app_name="giveaway"

urlpatterns = [
    path("show",show_giveaway,name="giveaway")
]
