from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Client,Devlopers
from django.contrib import messages



# Create your views here.

def index(request):

    if request.method == 'POST':
         name=request.POST['username']
         email=request.POST['email']
         cellno=request.POST['phone']
         info=request.POST['info']

         ne=Client(name=name,email=email,cellno=cellno,info=info)
         ne.save()

        
    
    return render(request,'index.html',{})


def devloper(request):
      
      if request.method == 'POST':
           expertise = request.POST['appointment-service']
           Fname= request.POST['first-name']
           lname= request.POST['last-name']
           email=request.POST['email']
           pno=request.POST['phone']
           desc=request.POST['disc']

           dev=Devlopers(expertise=expertise,Fname=Fname,lname=lname,email=email,pno=pno,desc=desc)
           dev.save()
           messages.success(request, 'Your information has been submitted successfully.')


      return render(request,'devloper.html')

   
