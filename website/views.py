from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    

    if request.method=="POST":
       fstname=request.POST['firstname']
       lstname=request.POST['lastname']
       dt=request.POST['date']
       eml=request.POST['email']
       trtt=request.POST['treatment']
       nte=request.POST['note']

       #send_mail(
        #fstname,
        #lstname,
        #dt,
        #eml,
        #trtt,
        #nte,
        #['john@codemy.com'],
       #   )

       return render(request,'appointment.html',{'fstname': fstname, 'lstname': lstname,'dt': dt, 'Eml': eml,'nte': nte,'trtt': trtt}) 


    else:
       return render(request,'home.html',{})


def contact(request):
     if request.method=="POST":
       fstname=request.POST['firstname']
       lstname=request.POST['lastname']
       dt=request.POST['date']
       eml=request.POST['email']
       trtt=request.POST['treatment']
       nte=request.POST['note']
       fullname=request.POST['first_name']
       email=request.POST['email1']
       msg=request.POST['message']
       
       return render(request,'appointment.html',{'fstname': fstname, 'lstname': lstname,'dt': dt, 'Eml': eml, 'nte': nte,'trtt': trtt}) 

     
     else:
       return render(request,'contact.html',{})


def about(request):
    return render(request,'about.html',{})


def news(request):
    return render(request,'news.html',{})

      
def patients(request):
    return render(request,'patients.html',{})


def services(request):
    return render(request,'services.html',{})

def appointment(request):
    return render(request,'appointment.html',{})    
