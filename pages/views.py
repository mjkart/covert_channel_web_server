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

            # parse and decode message
            request_parts = request.path.split(".")[0]
            byte_parts = [part.split("/") for part in request_parts]

            # add message to database
            new_row = models.Messages(uri=request.path, message=byte_parts[0])
            new_row.save()

        data = models.Messages.objects.all()
        context = {"table": data}
    return render(request, "home.html", context)
