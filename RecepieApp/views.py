from django.shortcuts import render,redirect
from django.contrib.messages import constants as messages
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login/")
def recepie(request):
    if request.method=="POST":
        data=request.POST
        r_name=data.get('rcepie_name')
        r_desc=data.get('recepie_description')
        r_image=request.FILES.get('recpie_image')
       
        Recepie.objects.create(
            rcepie_name=r_name,
            recepie_description=r_desc,
            recpie_image=r_image
        )
        return redirect('/recepies')
    querySet= Recepie.objects.all()
    context={'recepies':querySet}
    return render(request,"recepie.html",context)


def recepie_delete(request,id):
    query=Recepie.objects.get(id=id)
    query.delete()
    return redirect('/recepies/')

def update_recepie(request,id):
    querySet=Recepie.objects.get(id=id) 
    if request.method=="POST":
        data=request.POST
        r_name=data.get('rcepie_name')
        r_desc=data.get('recepie_description')
        r_image=request.FILES.get('recpie_image')

        querySet.rcepie_name=r_name
        querySet.recepie_description=r_desc
        if r_image:
            querySet.recpie_image=r_image
        querySet.save()
        return redirect('/recepies/')
    context={'recepie':querySet}
    return render(request,'update_recepies.html',context)

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login')
        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/recepies/')
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=User.objects.filter(username=username)

        if(user.exists()):
             messages.info                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          (request,'Username already taken')
             return redirect('/register/')
        user= User.objects.create (
           first_name= first_name,
           last_name=last_name,
           username=username
        )

        user.set_password(password)
        user.save()
        messages.info(request,'Account registered')
        return redirect('/register/')
    return render(request,"register.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')



