# pages/urls.py
from django.urls import path, re_path
from pages import views


urlpatterns = [
    re_path(
        r".*/*",
        views.covert_channel,
        name="home",
    ),
    path("results/", views.display_messages, name="messages"),
]
