from django.shortcuts import render, redirect, HttpResponse
from inquiry.models import Contact, Newsletter, Career, Applicants, Free_Trial
import datetime
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Contact

def contact_back(request) :

    if request.method == 'POST' :

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        service = request.POST.get('service', '')
        budget = request.POST.get('budget', '')
        currency = request.POST.get('currency', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        today = datetime.datetime.now()
        date = "At [{}:{}] On {} {}, {}".format(today.hour, today.minute, today.strftime('%B'), today.day, today.year)

        budget = str(budget) + " " + str(currency)

        # to kriosk
        message_ = "Hello, You have received new enquiry from website. Have a look at it. <br><br>" + "Name : " + name + "<br><br>Email : " + email + "<br><br>Phone : " + phone + "<br><br>Service : " + service + "<br><br>Budget : " + budget + "<br><br>Subject : " + subject + "<br><br>Message : " + message + "<br><br><br><br><br><br>Have a good one."

        title_ = "Web-Mail : Someone is trying to reach out to you for " + service

        email_ = EmailMessage(title_, message_, 'Kriosk Creata <mailer@krioskcreata.com>', ['info@krioskcreata.com'])

        email_.content_subtype = 'html'

        email_.send()

        # to user
        message__ = "Hello " + name + ",<br><br>" + "Thank you for contacting us. We have received your word and will get back to you very soon! <br><br><br><br><br><br> This is system generated email, do not reply to this. For more info, connect to us at info@krioskcreata.com or log onto krioskcreata.com." 

        title__ = "We have received your word regarding " + service

        email__ = EmailMessage(title__, message__, 'Kriosk Creata <mailer@krioskcreata.com>', [email])

        email__.content_subtype = 'html'

        email__.send()

        contact = Contact (
            name = name,
            email = email,
            phone = phone,
            service = service,
            budget = budget,
            subject = subject,
            message = message,
            date = date,
        )

        contact.save()

        msg = "Thank you for contacting, our team will look into it and will revert back very soon !"
        messages.success(request, msg)

        return redirect('contact')


    contact_back = Contact.objects.all()

    send = {
        'contact_back': contact_back,
    }

    return render(request, 'back/inquiry/contact_back.html', send)


@login_required
def contact_back_view(request, contact_pk) :

    try :
        contact_back = Contact.objects.get(pk=contact_pk)
    except :
        contact_back = None

    if not contact_back :
        msg = "Contact object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    send = {
        'contact_back': contact_back,
    }

    return render(request, 'back/inquiry/contact_back_view.html', send)


@login_required
def contact_back_delete(request, contact_pk) :

    try :
        contact_back = Contact.objects.get(pk=contact_pk)
    except :
        contact_back = None

    if not contact_back :
        msg = "Contact object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    
    contact_back.delete()


    msg = "Lead has been removed successfully !"
    messages.success(request, msg)

    return redirect('contact_back')


# Newsletter

def newsletter(request) :

    if request.method == 'POST' :

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        newsletter_all = Newsletter.objects.all()
        
        for NL in newsletter_all :
            if email == NL.email :
                msg = "You are already getting our Newsletters. You can always go ahead and add new email if you can't access your old one !"
                messages.success(request, msg)
                return redirect('blog')

        index = newsletter_all.count() + 1


        newsletter = Newsletter(
            index = index,
            name = name,
            email = email,
        )

        newsletter.save()

        msg = "Congratulations, now you will get super exciting emails from us !"
        messages.success(request, msg)

        return redirect('blog')

    else :
        msg = "Error : Something bad happened, try subscribing again !"
        messages.success(request, msg)

        return redirect('blog')


@login_required
def newsletter_list(request) :

    newsletter = Newsletter.objects.all().order_by('index')

    send = {
        'newsletter': newsletter,
    }

    return render(request, 'back/inquiry/newsletter.html', send)


@login_required
def newsletter_delete(request, newsletter_pk) :

    try :
        newsletter = Newsletter.objects.get(pk=newsletter_pk)
    except :
        newsletter = None

    if not newsletter :
        msg = "Newsletter object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    last = Newsletter.objects.last()

    if last == newsletter :
        newsletter.delete()

        msg = "Recipient has been removed successfully !"
        messages.success(request, msg)

        return redirect('newsletter_list')

    newsletter_all = Newsletter.objects.all().order_by('index')
    
    for NL in newsletter_all :
        if NL.index > newsletter.index :
            NL.index -= 1
            NL.save()

    newsletter.delete()

    msg = "Recipient has been removed successfully !"
    messages.success(request, msg)


    return redirect('newsletter_list')



# Career

@login_required
def career_list(request) :

    career = Career.objects.all()

    send = {
        'career': career,
    }

    return render(request, 'back/inquiry/career_list.html', send)



@login_required
def career_add(request) :

    if request.method == 'POST' :

        position_name = request.POST.get('position_name', '')
        position_number = request.POST.get('position_number', None)
        position_requirement = request.POST.get('detail1', '')
        status = request.POST.get('status', False)

        index = Career.objects.all().count() + 1

        career = Career(
            index = index,
            position_name = position_name,
            position_number = position_number,
            position_requirement = position_requirement,
            status = status,
        )

        career.save()

        msg = "New posting has been added, it will be visible on Career page within few moments !"
        messages.success(request, msg)


        return redirect('career_list')

    return render(request, 'back/inquiry/career_add.html')



@login_required
def career_edit(request, career_pk) :

    if request.method == 'POST' :

        index = request.POST.get('index', None)
        position_name = request.POST.get('position_name', '')
        position_number = request.POST.get('position_number', None)
        position_requirement = request.POST.get('detail1', '')
        status = request.POST.get('status', False)

        try :
            career = Career.objects.get(pk=career_pk)
        except :
            career = None

        if not career :
            msg = "Position object not found !"
            messages.success(request, msg)

            return redirect('error_back')
    

        career.index = index
        career.position_name = position_name
        career.position_number = position_number
        career.position_requirement = position_requirement
        career.status = status

        career.save()

        msg = "Posting has been edited, changes will be visible on Career page within few moments !"
        messages.success(request, msg)


        return redirect('career_list')

    

    try :
        career = Career.objects.get(pk=career_pk)
    except :
        career = None

    if not career :
        msg = "Position object not found !"
        messages.success(request, msg)

        return redirect('error_back')
    
    send = {
        'career': career,
    }

    return render(request, 'back/inquiry/career_edit.html', send)



@login_required
def career_delete(request, career_pk) :

    try :
        career = Career.objects.get(pk=career_pk)
    except :
        career = None

    if not career :
        msg = "Position object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    career.delete()

    msg = "Posting has been deleted, it will be removed from Career page within few moments !"
    messages.success(request, msg)

    return redirect('career_list')



# Applicants

def applicants_list(request) :

    if request.method == 'POST' :

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        position = request.POST.get('position', '')

        resume = request.FILES.get('resume', None)

        today = datetime.datetime.now()
        date = "At [{}:{}] On {} {}, {}".format(today.hour, today.minute, today.strftime('%B'), today.day, today.year)

        # to kriosk
        message_ = "Hello, You have received new application. Have a look at it. <br><br>" + "Name : " + name + "<br><br>Email : " + email + "<br><br>Phone : " + phone + "<br><brPosition : " + position + "<br><br><br><br><br><br>Have a good one."

        title_ = "Web-Mail : Received New Application for " + position

        email_ = EmailMessage(title_, message_, 'Kriosk Creata <mailer@krioskcreata.com>', ['info@krioskcreata.com'])

        email_.content_subtype = 'html'

        email_.attach(resume.name, resume.read(), resume.content_type)

        email_.send()

        # to user
        message__ = "Hello " + name + ",<br><br><br>" + "Thank you for showing interest in working with us. Your application has been submitted successfully. We will get back to you very soon. <br><br><br> Have a good day. <br><br><br><br><br><br> This is system generated email, do not reply to this. For more info, connect to us at info@krioskcreata.com or log onto krioskcreata.com." 

        title__ = "Successfully applied for position of " + position + " at Kriosk Creata"

        email__ = EmailMessage(title__, message__, 'Kriosk Creata <mailer@krioskcreata.com>', [email])

        email__.content_subtype = 'html'

        email__.send()


        applicants = Applicants(
            name = name,
            email = email,
            phone = phone,
            position = position,
            date = date,
            resume = resume,
        )

        applicants.save()

        msg = "Thank you for showing interest, we will get back to you very soon !"
        messages.success(request, msg)

        return redirect('career')

    applicants = Applicants.objects.all()

    send = {
        'applicants': applicants,
    }

    return render(request, 'back/inquiry/applicants_list.html', send)



@login_required
def applicants_delete(request, app_pk) :

    try :
        app = Applicants.objects.get(pk=app_pk)
    except :
        app = None

    if not app :
        msg = "Position object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    app.delete()

    return redirect('applicants_list')


# About Page Mails

def free_trial(request) :

    if request.method == 'POST':

        email = request.POST.get('email', '')

        free_all = Free_Trial.objects.all()

        for i in free_all :
            if i.email == email :
                
                msg = "This email is already used."
                messages.success(request, msg)

                return redirect('about')

        today = datetime.datetime.now()
        date = "At [{}:{}] On {} {}, {}".format(today.hour, today.minute, today.strftime('%B'), today.day, today.year)

        # to kriosk ===>
        # message_ = "Hello, You have received new free trial request. Have a look at it. <br><br>" + "Email : " + email + "<br><br><br><br><br><br>Have a good one."

        # title_ = "Web-Mail : Received New Free-Trial request"

        # email_ = EmailMessage(title_, message_, 'Kriosk Creata <info@surfica.tk>', ['zjiril@gmail.com'])

        # email_.content_subtype = 'html'

        # email_.send()

        # to user ===>
        # message__ = "Hello,<br><br><br>" + "Thank you for contacting us. We have received you request for free-trial and we will get back to you very soon! <br><br><br><br><br><br> This is system generated email, do not reply to this. For more info, connect to us at info@krioskcreata.com or log onto krioskcreata.com." 

        # title__ = "Success : Request for Free-Trial"

        # email__ = EmailMessage(title__, message__, 'Kriosk Creata <info@surfica.tk>', ['zjiril@gmail.com'])

        # email__.content_subtype = 'html'

        # email__.send()

        free = Free_Trial(
            email=email,
            date=date,
        )

        free.save()

        msg = "Your response has been submited successfully."
        messages.success(request, msg)

        return redirect('about')

    
    free = Free_Trial.objects.all()

    send = {
        'free': free,
    }

    return render(request, 'back/inquiry/free_trial_list.html', send)



@login_required
def free_trial_delete(request, free_pk) :

    try :
        free = Free_Trial.objects.get(pk=free_pk)
    except :
        free = None

    if not free :
        msg = "Position object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    free.delete()

    msg = "Applicant has been removed !"
    messages.success(request, msg)

    return redirect('free_trial')

