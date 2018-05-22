from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from app2 import models
from django.template import RequestContext
from django.template.context import RequestContext
from .models import users
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)
def accountlogin(request):
    template = get_template("login.html")
    username = request.POST.get('email','')
    password = request.POST.get('password','')
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect('/')
    else:
        return render(request,"login.html")
def ipmanage(request):
    template = get_template('servermanage.html')

    ips = models.hosts.objects.all()
    html = template.render(locals())
    return HttpResponse(html)
