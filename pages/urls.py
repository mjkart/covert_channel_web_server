# pages/urls.py
from django.urls import path
from pages import views


urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    path("", views.covert_channel, name="home"),
    # path("about/", AboutPageView.as_view(), name="about"),
]
