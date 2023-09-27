from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import school


def demo(request):
    obj = school.objects.all()

    return render(request, "index.html", {'result': obj})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is taken")
                return redirect('/register')
            else:

                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)

                user.save();
                return redirect('/login')

        else:
            messages.info(request,"password not match")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/form')
        else:
            messages.info(request,"login failed!!!")
            return redirect('/login')

    return render(request,"login.html")

def form(request):

    return render(request, "form.html")
def logout(request):
    auth.logout(request)

    return redirect("/")

def page(request):

    return render(request, "page.html")