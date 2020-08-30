from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hostels, Contact
from math import ceil
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    host = Hostels.objects.all()
    print(host)

    n = len(host)
    print(n)

    params = {'range': range(0, n), 'Hostel': host}
    return render(request, 'Find_Hostel/index.html', params)


def aboutus(request):

    return render(request, 'Find_Hostel/about.html')

# def hostels(request):
#     return render(request,'Find_Hostel/about.html')


def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save
    return render(request, 'Find_Hostel/contact.html')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        fname = request.POST['fname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        new_user = User.objects.create_user(name, email, password1)
        new_user.fname = fname
        new_user.save()
        messages.success(request, "user succcessfully created")
        return redirect("HostelHome")

    else:
        return HttpResponse("404 NOT FOUND")


def search(request):
    return render(request, 'Find_Hostel/about.html')


def hostels(request, myid):
    # fetch product using id
    host = Hostels.objects.filter(id=myid)
    print(host)

    n = len(host)
    print(n)

    params = {'Hostel': host[0]}

    return render(request, 'Find_Hostel/hostels.html', params)


def signin(request):
    if request.method == "POST":
        loginname = request.POST['loginname']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginname, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "logged in successfully")
            return redirect("HostelHome")
        else:
            messages.error(request, "invalid credentials")
            return redirect("HostelHome")
    else:
        return HttpResponse("404 NOT FOUND")


def signout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "logged out")
        return redirect("HostelHome")
    else:
        return HttpResponse("404 NOT FOUND")
