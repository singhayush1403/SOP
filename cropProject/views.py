from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>")

def v1(response):
    return HttpResponse("<h1>View 1!</h1>")

def profile(response):
    print(response)
    template = loader.get_template("registration/profile.html")
    return HttpResponse(template.render())