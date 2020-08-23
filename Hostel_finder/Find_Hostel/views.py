from django.shortcuts import render
from django.http import HttpResponse
from .models import Hostels,Contact
from math import ceil


# Create your views here.
def index(request):
    host=Hostels.objects.all()
    print(host)
    
    n=len(host)
    print(n)
    
    params={ 'range':range(0,n),'Hostel':host}
    return render(request,'Find_Hostel/index.html',params)

def aboutus(request):
    
    return render(request,'Find_Hostel/about.html')

# def hostels(request):
#     return render(request,'Find_Hostel/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name= request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save
    return render(request,'Find_Hostel/contact.html')


def register(request):
    return render(request,'Find_Hostel/register.html')

def search(request):
    return render(request,'Find_Hostel/about.html')


def hostels(request,myid):
    # fetch product using id
    host=Hostels.objects.filter(id=myid)
    print(host)
    
    n=len(host)
    print(n)
    
    params={'Hostel':host[0]}
   
    
    return render(request,'Find_Hostel/hostels.html',params)

