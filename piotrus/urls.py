from django.urls import path

from . import views

app_name = "piotrus"
urlpatterns = [
    path("", views.index, name="index"),
]