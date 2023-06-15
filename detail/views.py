from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from enroll.models import addbussi
from enroll.views import addbussi
from django.contrib import messages
# Create your views here.
def grocerry(request):
    data=addbussi.objects.filter(category='grocerry')
    return render(request,'detail/grocerry.html',{'name':'grocerry','data':data})
    
def hardware(request):
    hard=addbussi.objects.filter(category="hardware")
    return render(request,'detail/hardware.html',{'name':'hardware','hard':hard})

def fastfood(request):
    ftf=addbussi.objects.filter(category="fastfood")
    return render(request,'detail/fastfood.html',{'name':'fastfood','ftf':ftf})

def Mobile(request):
    mob=addbussi.objects.filter(category='mobile')
    return render(request,'detail/Mobile.html',{'name':'Mobile','mob':mob})

def gift(request):
    gif=addbussi.objects.filter(category='gift')
    return render(request,'detail/gift.html',{'name':'gift','gif':gif})

def jewellery(request):
    jwel=addbussi.objects.filter(category='jewellery')
    return render(request,'detail/jewellery.html',{'name':'jewellery','jwel':jwel})

def electronic(request):
    electro=addbussi.objects.filter(category='electronic')
    return render(request,'detail/electronic.html',{'name':'electronic','electro':electro})

def watch(request):
    wth=addbussi.objects.filter(category='watch')
    return render(request,'detail/watch.html',{'name':'watch','wth':wth})

def steel(request):
    stl=addbussi.objects.filter(category='steel')
    return render(request,'detail/steel.html',{'name':'steel','stl':stl})

def Fashion(request):
    fsh=addbussi.objects.filter(category='fashion')
    return render(request,'detail/Fashion.html',{'name':'Fashion','fsh':fsh})

def pharmacy(request):
    pharm=addbussi.objects.filter(category='pharmacy')
    return render(request,'detail/pharmacy.html',{'name':'pharmacy','pharm':pharm})

def footwear(request):
    foot=addbussi.objects.filter(category='footwear')
    return render(request,'detail/Footwear.html',{'name':'footwear',"foot":foot})

def computer(request):
    comp = addbussi.objects.filter(category='computer')
    return render(request,'detail/computer.html',{'name':'computer', 'comp':comp})

def coffee(request):
    cof = addbussi.objects.filter(category='coffee')
    return render(request,'detail/coffee.html',{'name':'coffee','cof':cof})

