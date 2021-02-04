from django.shortcuts import render, redirect, HttpResponse
from inquiry.models import Contact
import datetime
from django.contrib import messages


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






