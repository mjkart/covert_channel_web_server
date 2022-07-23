from wsgiref.util import request_uri
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from pages import models

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


def covert_channel(request):
    if request.method == "GET":
        if request.path != "/":
            message = models.Messages(uri=request.path)
            message.save()
            messages = models.Messages.objects.all()
            context = {"messages": messages, "test": "context test"}
    return render(request, "home.html", context)
