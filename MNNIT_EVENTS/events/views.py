from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import events,query,collegeName,campusAmbassador,fullUser,ticket


# Create your views here.

def index(request):

    ev = events.objects.all()

    return render(request,'index.html',{'events': ev})


def register(request):

    colNames = collegeName.objects.all()
    
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        college_name = request.POST['college_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username already exist')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exist')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                newUser = fullUser.objects.create(college_name=college_name,phone_number=phone_number,user=user)
                user.save()
                newUser.save()
                return redirect('/')
        else:
            messages.error(request,'password not matching')
        
        

    return render(request,'signup.html',{'colNames':colNames})

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
    return redirect('/')

def details(request,evId):
    choosen_event = events.objects.filter(id=evId)
    curr_user = request.user
    curr_user_request = campusAmbassador.objects.filter(user_id=curr_user.id, event_id=evId)
    if not len(curr_user_request):
        return render(request,'event_page.html',{'choosen_event': choosen_event[0],'present':False,'approval':False})
    else:
        approval = curr_user_request[0].approval
        return render(request,'event_page.html',{'choosen_event': choosen_event[0],'present':True,'approval':approval})
        



def sendQuery(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message =  request.POST['message']

        qu = query(name=name,email=email,subject=subject,message=message)
        qu.save()

    
    return redirect('/')

def requestCA(request,evId):
    choosen_event = events.objects.filter(id=evId)
    if request.method=="POST":
        name = request.POST['username']
        user_id = request.POST['user_id']
        event_id = choosen_event[0].id
        previous_experience = request.POST['previousExperience']

        CA = campusAmbassador(name=name, user_id=user_id, event_id=event_id, previous_experience=previous_experience)
        CA.save()
        ev = events.objects.all()
        return redirect('/details/',{'events':ev})
    return render(request,'ca_request.html',{'choosen_event': choosen_event[0]})

def payment(request,evId):
    choosen_event = events.objects.filter(id=evId)
    curr_user = request.user
    curr_full_user = fullUser.objects.filter(user_id=curr_user.id) 
    if request.method=="POST":
        name = curr_user.first_name
        event_name = request.POST['eventName']
        user_id = curr_user.id
        event_id = evId
        college_name = curr_full_user[0].college_name
        tik = ticket(name=name,event_name=event_name,user_id=user_id,event_id=event_id,college_name=college_name)
        tik.save()
        
    return render(request,'payment_page.html',{'choosen_event': choosen_event[0]})


def userList(request,evId):
    curr_user = request.user
    curr_full_user = fullUser.objects.filter(user_id=curr_user.id) 
    sameCollegeUser = fullUser.objects.filter(college_name=curr_full_user[0].college_name)
    return render(request,'user_list.html',{'sameCollegeUser':sameCollegeUser,'evId':evId})



