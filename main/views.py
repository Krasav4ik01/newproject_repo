from dataclasses import field
from hashlib import new
from multiprocessing import context
from sre_constants import SUCCESS
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render

# from main.decarators import allowed_users, unauthenticated_user
from . models import *
from .forms import *
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .decorators import admin_only, unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.l
from django.contrib.auth.models import User

def addpage(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        
        
        if form.is_valid():
            
            form.save()
            
            return redirect('test')
            
        else:
            error = 'Форма была неверной'

    form = NewsForm()
    data = {
        
        'form': form,
        'error': error
    }
    return render(request, 'main/index1.html', data)








# def news(request):
#     p = Login.objects.all()
#     return render(request, 'main/news.html',{'p':p})





# def send_message(request):
#     send_mail("There is title", 
#     "There is content", 
#     "200103424@stu.sdu.edu.kz",
#     ["200103424@stu.sdu.edu.kz"], fail_silently=False)
#     return render(request, 'main/labka.html')
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # email = EmailMessage(
    # "There is title", 
    # "There is content", 
    # "200103424@stu.sdu.edu.kz",
    # ["200103424@stu.sdu.edu.kz"],
    # headers={'Message-ID': 'foo'})
    # email.attach_file('')
    # email.send(fail_silently=False)
    












def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
       
      
        if password1 == password2:
            user = User.objects.create_user(username=username,password = password1, email=email, first_name=first_name, last_name=last_name)
           
            user.save()
            return redirect('test')
        else:
            return HttpResponse('Error!')

    else:
        return render(request, 'main/register.html')



##############################################################################################################################






def index(request):
    
    if request.method == "POST":
        form = MvideoForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-upload')
    else:
        form = MvideoForm()
        
    var = {'form': form}
    return render(request, 'main/index.html', var)












def test(request):
    las = Login.objects.last()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], '200103424@stu.sdu.edu.kz', ['200103424@stu.sdu.edu.kz'], fail_silently=True)
            if mail:
                messages.success(request, 'Email is send!')
                return redirect('test')
            else:
                messages.error(request,'Sending error!')
        else:
            messages.error(request, 'Register error!')
    else:
        form=ContactForm()
    return render(request, 'main/test.html', {'form':form, 'las':las})                        

