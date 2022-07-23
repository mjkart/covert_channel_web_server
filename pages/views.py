from wsgiref.util import request_uri
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def covert_channel(request):
    if request.method == "GET":
        context = {"ur": request_uri, "test": "context test"}
    return render(request, "home.html", context)
