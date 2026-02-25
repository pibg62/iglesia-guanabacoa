from django.urls import path
from .views import HomeView, AboutView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("acerca-de/", AboutView.as_view(), name="about"),
]
