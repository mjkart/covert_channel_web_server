# pages/urls.py
from django.urls import path, re_path
from pages import views


urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    re_path(
        r".*",
        views.covert_channel,
        name="home",
    ),
    # path("about/", AboutPageView.as_view(), name="about"),
]
