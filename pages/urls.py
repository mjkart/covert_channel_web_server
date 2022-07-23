# pages/urls.py
from django.urls import path, re_path
from pages import views


urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    re_path(
        r"[a-zA-Z]*/[a-zA-Z]*[^a-zA-Z0-9_]*[a-zA-Z]*[^a-zA-Z0-9_]*[a-zA-Z]*",
        views.covert_channel,
        name="home",
    ),
    # path("about/", AboutPageView.as_view(), name="about"),
]
