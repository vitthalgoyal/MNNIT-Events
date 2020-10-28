from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import events,query,collegeName,campusAmbassador,fullUser,ticket
from django.core.mail import send_mail


# Create your views here.

def index(request):

    ev = events.objects.all()

    return render(request,'index.html',{'events': ev})

def developers(request):
    return render(request,'developers.html')


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
    if ticket.objects.filter(user_id=curr_user.id, event_id=evId).count()>0 :
        is_user_purchased_ticket=True
    else :
        is_user_purchased_ticket=False

    if not len(curr_user_request):
        return render(request,'event_page.html',{'choosen_event': choosen_event[0],'present':False,'approval':False,'purchased':is_user_purchased_ticket})
    else:
        approval = curr_user_request[0].approval
        return render(request,'event_page.html',{'choosen_event': choosen_event[0],'present':True,'approval':approval,'purchased':is_user_purchased_ticket})
        



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
        return redirect('/details/'+str(evId))
    return render(request,'ca_request.html',{'choosen_event': choosen_event[0]})

def payment(request,evId):
    choosen_event = events.objects.filter(id=evId)
    curr_user = request.user
    curr_full_user = curr_user.fulluser
    if request.method=="POST":
        name = curr_user.first_name
        event_name = request.POST['eventName']
        user_id = curr_user.id
        event_id = evId
        college_name = curr_full_user.college_name
        tik = ticket(id_ticket=curr_full_user,name=name,event_name=event_name,user_id=user_id,event_id=event_id,college_name=college_name)
        tik.save()
        return redirect('/details/'+str(evId))
        
    return render(request,'payment_page.html',{'choosen_event': choosen_event[0]})


def userList(request,evId):
    curr_user = request.user
    curr_full_user = curr_user.fulluser
    sameCollegeUserPurchsed = fullUser.objects.filter(college_name=curr_full_user.college_name , ticket__event_id=evId)
    sameCollegeUserNotPurchsed = fullUser.objects.filter(college_name=curr_full_user.college_name).exclude(id__in=sameCollegeUserPurchsed)
    return render(request,'user_list.html',{'sameCollegeUserPurchsed':sameCollegeUserPurchsed,'sameCollegeUserNotPurchsed':sameCollegeUserNotPurchsed,'evId':evId})


def profile(request):
    curr_user = request.user
    curr_full_user = curr_user.fulluser
    return render(request,'profile.html',{'curr_user':curr_user,'curr_full_user':curr_full_user})


def sendRequest(request,user_id,evId):

    req_user=User.objects.get(id=user_id)

    choosen_event=events.objects.get(id=evId)
    send_mail('Request from '+str(request.user.first_name)+' '+str(request.user.last_name),
    'Dear '+str(req_user.first_name) +'\n\n'

'We would like to extend an open invitation to all users of ' + str(request.user.fulluser.college_name) + ' to the '+ str(choosen_event.name)+'\n'
'Please book your tickets well in advanced , it would be appreciated. We hope to see everyone there.\n\n'

'For more information about the event please visit event official website '+ choosen_event.url +"\n\n"

'Sincerely,\n'+str(request.user.first_name)+' '+str(request.user.last_name)

,
    'vitthalgoyal2002@gmail.com',
    [req_user.email]
    )
    return render(request,'sendRequest.html',{'evId':evId})

def sendReminder(request,user_id,evId):

    req_user=User.objects.get(id=user_id)

    choosen_event=events.objects.get(id=evId)
    send_mail('Reminder from '+str(request.user.first_name)+' '+str(request.user.last_name),
    'Dear '+str(req_user.first_name) +'\n\n'

'We would like to remind you to the event '+ str(choosen_event.name)+' for which you have already purchased the ticket \n'
'Please visit the venue well in time , it would be appreciated. We hope to see you there.\n\n'


'Sincerely,\n'+str(request.user.first_name)+' '+str(request.user.last_name)

,
    'vitthalgoyal2002@gmail.com',
    [req_user.email]
    )
    return render(request,'sendReminder.html',{'evId':evId})



