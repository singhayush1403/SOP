from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url="/accounts/login")
def index(response):
    return HttpResponse("<h1>tech with tim!</h1>")

def v1(response):
    return HttpResponse("<h1>View 1!</h1>")
    
@login_required(login_url='/accounts/login')
def profile(response):
    print(response.user.is_authenticated)
    context = {
      "user":response.user
      }
    #template = loader.get_template("registration/profile.html")
    return render(response,"registration/profile.html",context)