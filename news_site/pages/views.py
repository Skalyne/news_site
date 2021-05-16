from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def homePageView(request):
    return HttpResponse("Hello world")

class NewsPageView(TemplateView):
    template_name="home.html"
