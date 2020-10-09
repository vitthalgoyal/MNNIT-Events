from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')


def register(request):
    
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exist')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                print("User created")
                return redirect('/')
        else:
            messages.error(request,'password not matching')
        
        

    return render(request,'signup.html')

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password')
    
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'index.html')
