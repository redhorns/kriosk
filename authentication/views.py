from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from authentication.models import Auth_Code
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import random



def myregister(request) :

    if request.method == "POST" :

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        

        if password1 != password2 :
            msg = "Holy guacamole! You must have screwed up something. Lemme check what's wrong... a'ight, it seems like your passwords didn't match !"
            messages.success(request, myregister)

            return redirect(myregister)

        if len(password1) < 6 :
            msg = "Holy guacamole! You must have screwed up something. Lemme check what's wrong... a'ight, it seems like your password wasn't minimum 6 chars long !"
            messages.success(request, msg)

            return redirect('myregister')

        # success
        if len(User.objects.filter(username=email)) == 0 :

            user = User.objects.create_user(username=email, email=email, password=password1, first_name=username, is_active=False, is_superuser=False)

            auth_code = random.randint(1000,9999)

            auth__code = Auth_Code(
                auth_user = user,
                auth_code = auth_code,
                auth_is_used = False,
            )
            auth__code.save()

            message = "Hey " + "<b>" + username + "</b>" + "<br><br>" + "Greetings, " + "<br><br><br>" + "Your Authentication Code is - " + "<b>"  + str(auth_code) + "</b>"  + "<br><br><br><br>" + "Regards, Team -"

            email_send = EmailMessage("Authentication Code for www.-.com", message, settings.EMAIL_HOST_USER, [email])

            email_send.content_subtype = 'html'
            email_send.send()


            msg = "Voilà, Activation Auth-Code has been sent to " + str(email)
            messages.success(request, msg)

            return redirect('myactivation_end')
            
        else : 
            msg = "Voila, you are already associated with us. Try signing in again !"
            messages.success(request, msg)

            return redirect('myregister')


    return render(request, 'back/authentication/register.html')


def mylogin(request) :

    if request.method == 'POST' :

        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user_ = User.objects.get(username=email)

        if user_.is_active :
            print("user is active !")
        else :
            print("user is not active !")

        user = authenticate(username=email, password=password)

        if user != None :
            
            login(request, user)

            if user.is_active :
                msg = "You are active now !"
                messages.success(request, msg)

                return render(request, 'back/authentication/status.html')
            else :
                msg = "You are not active now!"
                messages.success(request, msg)

                return render(request, 'back/authentication/status.html')

        else : 

            msg = "Wrong ID/PASSWORD !"
            messages.success(request, msg)

            return redirect('mylogin')



    return render(request, 'back/authentication/login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')



def myactivation_initiate(request) :

    if request.method == 'POST' : 

        email_ = request.POST.get('email', '')
        
        # getting : User
        try :
            user = User.objects.get(username=email_)
        except :
            msg = "Email doesn't exists in our records, try registering yourself up !"
            messages.success(request, msg)

            return redirect('myregister')

        # getting : Auth_Code
        try :
            auth__code = Auth_Code.objects.get(auth_user=user)
        except :
            msg = "Failed due to internal error, Try registering again or contact us !"
            messages.success(request, msg)

            return redirect('myregister')

        # checking : flagged
        if auth__code.auth_is_flagged == True :
            msg = "Your account is blocked by admin due to suspicious activities !"
            messages.success(request, msg)

            return redirect('myregister')



        if user.is_active != True :

            if auth__code :

                message = "Hey " + "<b>" + user.first_name + "</b>" + "<br><br>" + "Greetings, " + "<br><br><br>" + "Your Authentication Code is - " + "<b>"  + str(auth__code.auth_code) + "</b>"  + "<br><br><br><br>" + "Regards, Team -"

                email_send = EmailMessage("Authentication Code for www.-.com", message, settings.EMAIL_HOST_USER, [user.email])

                email_send.content_subtype = 'html'
                email_send.send()

            else :
                msg = "Failed due to internal error, Try registering again or contact us !"
                messages.success(request, msg)

                return redirect('myregister')


            return redirect('myregister')

        elif user.is_active == True :
            msg = "Your account is already activated, try signing in !"
            messages.success(request, msg)

            return redirect('mylogin')

        

        return redirect('myactivation_end')




    return render(request, 'back/authentication/activation_init.html')


def myactivation_end(request) :

    if request.method == 'POST' :

        email_ = request.POST.get('email', '')
        auth_code_ = request.POST.get('auth_code', '')
        
        try :
            user = User.objects.get(username=email_)
        except :
            msg = "Email doesn't exists in our records, try registering yourself up !"
            messages.success(request, msg)

            return redirect('myregister')
        
        try :
            auth__code = Auth_Code.objects.get(auth_user=user)
        except :
            msg = "Failed due to internal error, Try registering again or contact us !"
            messages.success(request, msg)

            return redirect('myregister')

        if int(auth_code_) == auth__code.auth_code :

            if user.is_active != True :

                user.is_active = True
                user.save()

                auth__code.auth_is_used = True
                auth__code.save()

                return HttpResponse("Success")

            elif user.is_active == True :
                msg = "Your account is already activated, try signing in !"
                messages.success(request, msg)

                return redirect('mylogin')


        else :
            msg = "Auth Code did not match !"
            messages.success(request, msg)

            return redirect('myactivation_initiate')


    return render(request, 'back/authentication/activation_end.html')


