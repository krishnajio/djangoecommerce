from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User,auth
from .gmod import Userdata 
# Create your views here.


def logout(request):
    request.session['username']=None
    messages.info(request,"You are successfully logout")
    return redirect("/")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        Userdata.cusername= username
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            Userdata.cuserid = user.id
            print(Userdata.cuserid)
            request.session.set_expiry(300)
            return redirect("/")
        else:
            messages.info(request,"Invalid Crenditail")
            request.session['username']=None
            return redirect("/")
    else:
         return render(request,'users/login.html')        

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,f'Welcome { username},your account has been created')
                return redirect('/')

    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})