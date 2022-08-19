from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout as auth_logout, login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from student.models import ResultStyleHideUnHide,UserEnrollment
 
def register(request):
    context={}
    x2=ResultStyleHideUnHide.objects.last()
    context['x2']=x2
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        enroll=request.POST.get('enroll')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username Taken')
                return render(request,'users/signup.html',context)
            elif len(password) <8:
                messages.warning(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return render(request,'users/signup.html',context)
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email Taken')
                return render(request,'users/signup.html',context)
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                enrollment_obj=UserEnrollment.objects.create(enrollment_no=enroll,user=entry)
                enrollment_obj.save()
                
                messages.success(request,'Your Account Has been created successfully!')
                return HttpResponseRedirect(reverse('users:login'))
        else:
            messages.warning(request,'Password and confirm password didn"t match')
    return render(request,'users/signup.html',context)

def signup(request):
    context={}
    x2=ResultStyleHideUnHide.objects.last()
    context['x2']=x2
    try:
        if request.user.is_authenticated:
            messages.error(request,'Something went wrong!')
            return redirect('/')
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            print('username : ',username)
            user = authenticate(request, username=username, password=password)
            print('user : ',user)
            if user is not None:
                login(request, user)
                messages.success(request,'logged in successful')
                return redirect('/')
            else:
                messages.error(request,'Please enter correct Username and Password !!')
                return redirect('users:login')
            
    except Exception as e:
        print('Login Exception',e)
    return render(request,'users/login.html',context)
def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect(reverse('home2'))