# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import register_model
from django.shortcuts import render
from .forms import SignupForm
import hashlib
from django.contrib import auth
from django.contrib.auth import authenticate, login
# authenticate is for to autnticate username and paswd and login is for session_id
from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
#from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
#from django.core.context_processors import csrf
from django.template import RequestContext
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import hashlib
from django.contrib.auth.hashers import make_password , check_password



# Create your views here.
def user_signup(request):
    try:

    #csrfContext = RequestContext(request)
        print "hey"
        if request.method == 'POST':
            #form = SignupForm(request.POST or None)
            #if form.is_valid():
            #password = form.cleaned_data['password']
            password = request.POST['password']
            print password
            #form.password = make_password(password)
            #pswd = form.password
            #print pswd
            #user = form.save(commit=False)
            #user.is_active = False
            #user.save()
            #userobj = form.cleaned_data
            #username = userobj['username']
            #email = userobj['email']
            #raw_password = userobj['password']
            user = register_model()
            username = request.POST['username']
            email = request.POST['email']
            user.firstname = request.POST['first_name']    
            user.lastname = request.POST['last_name']    
            user.username = username   
            user.password = make_password(password)    
            user.email = email    
            user.contact_no = request.POST['contact_no']  
            if not (register_model.objects.filter(username=username).exists() or register_model.objects.filter(email=email).exists()):
                #user.password = make_password(password)
                pd = user.password
                print "encrpted passwd is"
                print pd
                user.save()
                current_site = get_current_site(request)
                subject = 'Activate your account.'
                message = render_to_string('user_model/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMessage(subject,message,to=[to_email])
                email.send()
                return HttpResponse("Activation link is sent to an email, Please activate your account")
                #return render(request, 'S_W/confirmaton.html')
            else:
                context = {
                'message': "Username or email exist please try something different"
            }
                return render(request,'user_model/error.html', context)
        else:
            return render(request, 'user_model/register.html')
    except:
        #return render(request, 'user_model/error.html')    
        return render(request, 'user_model/register.html')

#def make_password(password):
    #hash = hashlib.md5(password).hexdigest()
    #return hash


def activate(request, uidb64, token):
    try:
        #return HttpResponse('hey')
        #return HttpResponse(uidb64)
        #uidb64 = request.GET.get('uidb64')
        #return HttpResponse(uidb64)
        uid = force_text(urlsafe_base64_decode(uidb64))
        #return HttpResponse(uid)
        user = register_model.objects.get(pk=uid)
        #return HttpResponse(user)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        #return HttpResponse("heyyyyyyyyyyyyy")
        #user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponseRedirect(reverse('user_login'))
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


#def check_password(password):
#    paswd = make_password(password)
#    return paswd


def user_login(request):
        #context = {}
        #csrfContext = RequestContext(request)
        if request.method == 'POST':
            #con = {}
            username = request.POST['username']
            password = request.POST['password']
            #return HttpResponse(password)
            #user = register.objects.get(username=username)
            #return HttpResponse(user.password)

            passw = register_model.objects.get(username=username)
            passwordd = passw.password
            print (passw.password)
            passwd = check_password(password, passwordd)
            print (passwd)
            #user = authenticate(username = username, password = password)
            if passwd:
                user = register_model.objects.get(username=username , password = passwordd)
            else:
                print "error"
            #return HttpResponse(user)
            #return HttpResponse(user.username)
            if user:
                print(user)
                #return HttpResponse(user.id)
                #request.session['signupp_id'] = user
                user.is_active = True
                print (user.id)
                request.session['user_id'] = user.id
                new_id = user.id
                user.save()
                #print (request.session['user_id'])
                #return render(request,'S_W/error.html',{'username':username})
                #login(request, user)
                #uu = request.session['signupp_id']
                #return HttpResponse(uu)
                #request.session['email_confirmed'] = True 

                return HttpResponseRedirect(reverse('user_home'))
            #else:
                #context['error'] = "Error in Connection"
                #return render(request, 'S_W/error.html', context)
        else:
            #context[error] = "ERROR"
            #return HttpResponse("eeeoooorrrrooror")
            return render(request, 'user_model/login.html')


def password_reset(request):
    print "hey"
    if request.method == 'POST':
        print "problem"
        email = request.POST['email']
        try:
            users = register_model.objects.get(email=email)
        except:
            users = None

        print email

        if users is not None:
            print "password reset process"
            context = {
                "message" : "you are registered user"
            }
            user = users
            user.save()
            print user
            current_site = get_current_site(request)
            subject = 'rest password of your account.'
            message = render_to_string('user_model/password_reset_confirm.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            })
            to_email = email
            Email = EmailMessage(subject,message,to=[to_email])
            Email.send()
            request.session['user_id'] = user.id
            new_id = user.id
            print "session is"
            print new_id
            return HttpResponse("Activation link is sent to an email, Please activate your account")
            #return render(request, 'S_W/confirmaton.html')

        else:
            print "Something wents wrong"
            print "please try again with different ID"
            context = {
                "message" : "you are not registered user"
            }

    else:
        context = {
            "message" : "Please Enter your Email......"
        }
        print "Sorry"

    return render(request, 'user_model/password_reset.html', context)


def password_reset_new(request):

        new_id = request.session['user_id']
        print new_id
        if new_id is not None:
            print new_id
            if request.method == 'POST':
                try:
                    user = register_model.objects.get(id = new_id)
                    print "User is"
                    print user
                except:
                    user = None
                if user is not None:           
                    print new_id
                    old_password = request.POST['old_password']
                    new_password = request.POST['new_password']
                    print old_password
                    print user.password
                    confirm_password = make_password(old_password)
                    #print password

                    if (old_password == new_password):
                        print "passwords are same"
                        user.password = confirm_password
                        print user.password
                        user.is_active = True
                        user.email_confirmed = True
                        user.save()
                        
                        context = {
                            "message": "your password is changed successfully",
                            "conn": True
                        }
                        

                        # now redirect a page on user_login and set a sleep time of 5 sec to redirect it automaticaly
                        # ye dekhna hai apan ko kal kii kesse
                        # ki back jaaane pr session expire ho jaaaye
                        # fir wapas login page pr redirect ho and new sessions bane
                        # 

                    else:
                        print "passswords are not same"
                        
                        context = {
                            "message": "your password is not changed, both passwords are not same",
                        }

                    
                
                else:
                    print "user is none"
                # print user
                # print user.firstname
                # print user.password
                # user.password = make_password(password)
                # user.save()
            
                # print user.password

                # print "hey"

                    context = {
                        "message": "your password is changed successfully"
                    }

            else:
                print "you are on secand path"

                context = {
                        "message": "you are on wrong path"
                    }

        else:
            context = {
                "message" : "Please reset your password"
            }

        return render(request, 'user_model/reset_pass.html', context)


def activate_password(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = register_model.objects.get(pk = uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        #return HttpResponse("heyyyyyyyyyyyyy")
        #user.is_active = True
        user.save()
        #login(request, user)
        return HttpResponseRedirect(reverse('password_reset_new'))

        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

    else:
        return HttpResponse('Activation link is invalid!')




def user_home(request):

    try:
        #context = {}
        #if request.session.get('email_confirmed'):
        request.session.set_expiry(300)
        try:
            new_id = request.session['user_id']
            print (new_id)
            print("user id is")
        except:
            HttpResponse("Error")


        try:
            if new_id:
                print ("in New_id")
                print (new_id)
                hello = request.session['user_id']
                USER = register_model.objects.get(id = new_id)  
                print (hello)
                print ("user is below")
                print (USER)
                context = {'user':USER}
                return render(request,'user_model/error.html',context)
                #user = request.user
                #return render(request,'S_W/error.html',context)
            else:
                context={
                    "message": "hey "
                }
                return render(request,'user_model/error.html', context)
        except:
            HttpResponse("error")

    except:
        return render(request,'user_model/error.html')    
