from django.shortcuts import render
from enroll.models import addbussi
from django.contrib import messages
from enroll.models import contact
# Create your views here.
def home(request):
    return render(request,'enroll/index.html')

def aboutus(request):
    return render(request,'enroll/aboutus.html')

def contactus(request):
    messages.info(request," Note: if you have any query related website ,Kindly fill the Form Below!!")
    if request.method=="POST":
        name=request.POST.get('fname',False)
        lname=request.POST.get('lname',False)
        email=request.POST.get('email',False)
        topic=request.POST.get('topic',False)
        message=request.POST.get('messagefield',False)
        if len(name)<2 or len(lname)<3 :
            messages.error(request,"Please fill the Form correctly ")
        elif len(topic)<5 or len(message)<5 :
            messages.error(request,"Please fill the Form correctly ")
        else:
            dta=contact(name=name,lname=lname,email=email,topic=topic,message=message)
            dta.save()
            messages.success(request,"Thanks!! your request is sent to our system .")
            messages.info(request,"we will back soon with reply .thanks again for your support")
        
    return render(request,'enroll/contactus.html')

def addbusiness(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        shopad = request.POST.get('address',False)
        category = request.POST.get('category',False)
        phone = request.POST.get('phone',False)
        rating=request.POST.get('rating',False)
        url=request.POST.get('url',False)
        imagelink=request.POST.get('imagelink',False)
        timing_to=request.POST.get('timing_to',False)
        timing_from=request.POST.get('timing_from',False)
        if len(name)<2 or len(email)<3 :
            messages.error(request,"Please fill the Form correctly ")
        elif len(phone)<2 or len(shopad)<3 :
            messages.error(request,"Please fill the Form correctly ")
        else:
            Metadata=addbussi(name=name,email=email,phone=phone,address=shopad,category=category,rating=rating,url=url,timing_to=timing_to,timing_from=timing_from,imagelink=imagelink)
            Metadata.save()
            messages.success(request,"Success !! your shop details has been sent for verification")
            messages.info(request,"After varification we will connect your Shop details with Mybusiness")
        
    return render(request,'enroll/mybussi.html')

def launch(request):
    return render(request,'enroll/new.html')

def search(request):
    query=request.GET['query']
    if len(query)>15:
        allposts=[]
    else:
       allposts=addbussi.objects.filter(rating__icontains=query)
    if allposts.count()==0:
        messages.error(request,"PLease fill the text correctly!!")
    params={'allposts':allposts}
    return render(request,'enroll/search.html',params)

# def search(request):
#     if request.method=="GET":
#         query=request.GET.get('query')

#         if query is not None:
#             results=addbussi.objects.filter(name__icontains='query')
#             return render(request,'enroll/search.html',{'alldata':results})
#         else:
#             messages.error(request,"Please Enter the Valid Input!!!")