from django.shortcuts import render, redirect
from django.http import HttpResponse
from panel.models import Portfolio, Portfolio_Image, Home, Service_Sub, Service
from django.contrib import messages
import datetime
from django.utils.safestring import mark_safe
import json
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain


# Home

def home_back(request) :

    if request.method == 'POST' :

        home_count = Home.objects.all().count()

        if home_count >= 9 :
            msg = "Sorry, There already are 9 objects. Inorder to add new, delete any of existing object !"
            messages.success(request, msg)

            return redirect('home_back')


        index = request.POST.get('index', None)
        title = request.POST.get('title', '')
        image1 = request.FILES.get('image1', None)

        home_back = Home (
            index = index,
            title = title,
            image1 = image1,
        )

        home_back.save()

        msg = "Home Image object has been added successfully !"
        messages.success(request, msg)

        return redirect('home_back')



    home_back = Home.objects.all()

    index_next = home_back.count() + 1

    send = {
        'home_back': home_back,
        'index_next': index_next,
    }

    return render(request, 'back/panel/home_back.html', send)



def home_edit_back(request, home_pk) :

    if request.method == 'POST':

        try :
            home_back = Home.objects.get(pk=home_pk)
        except :
            home_back = None

        if not home_back :

            msg = "Home Image Object not found, try going back and refreshing the page !"
            messages.success(request, msg)

            return redirect('error_back')

        index = request.POST.get('index', None)
        title = request.POST.get('title', '')
        image1 = request.FILES.get('image1', None)

        if image1 != None :
            if home_back.image1 :
                default_storage.delete(home_back.image1.path)
            home_back.image1 = image1

        home_back.index = index
        home_back.title = title

        home_back.save()

        msg = "Edits made to Home Image object has been applied successfully !"
        messages.success(request, msg)

        return redirect('home_back')



    try :
        home_back = Home.objects.get(pk=home_pk)
    except :
        home_back = None

    if not home_back :

        msg = "Home Image Object not found, try going back and refreshing the page !"
        messages.success(request, msg)

        return redirect('error_back')


    send = {
        'home_back': home_back,
    }

    return render(request, 'back/panel/home_edit_back.html', send)



def home_delete_back(request, home_pk) :

    try :
        home_back = Home.objects.get(pk=home_pk)
    except :
        home_back = None

    if not home_back :

        msg = "Home Image Object not found, try going back and refreshing the page !"
        messages.success(request, msg)

        return redirect('error_back')

    home_back.delete()

    msg = "Home Object has been deleted successfully !"
    messages.success(request, msg)


    return redirect('home_back')





# Portfolio

def back_portfolio_list(request) :

    portfolio = Portfolio.objects.all().order_by('index')

    send = {
        'portfolio': portfolio,

    }

    return render(request, 'back/panel/portfolio_list.html', send)



def back_portfolio_add(request) :

    if request.method == 'POST' :

        client_name = request.POST.get('client_name', '')
        client_tagline = request.POST.get('client_tagline', '')
        services = request.POST.get('services', '')
        detail = request.POST.get('detail1', '')

        image1 = request.FILES.get('image1', None)
        image_wide = request.POST.get('image_wide', None)

        # auto indexing
        last = Portfolio.objects.last()
        if last :
            index = last.index + 1
        else :
            index = 1

        # checking : image is wide
        if image_wide :
            image_wide = image_wide
        else :
            image_wide = False

        portfolio = Portfolio(
            index = index,
            client_name = client_name,
            client_tagline = client_tagline,
            services = services,
            detail = detail,
            image1 = image1,
            image_wide = image_wide,
        )

        portfolio.save()

        msg = "New client portfolio has been added successfully !"
        messages.success(request, msg)

        return redirect('back_portfolio_list')



    return render(request, 'back/panel/portfolio_add.html')



def back_portfolio_edit(request, portfolio_pk) :

    if request.method == 'POST' :

        try :
            portfolio = Portfolio.objects.get(pk=portfolio_pk)
        except :
            portfolio = None

        if not portfolio :

            msg = "Portfolio not found, try going back and refreshing the page !"
            messages.success(request, msg)

            return redirect('error_back')


        index = request.POST.get('index', None)
        client_name = request.POST.get('client_name', '')
        client_tagline = request.POST.get('client_tagline', '')
        services = request.POST.get('services', '')
        detail = request.POST.get('detail1', '')

        image1 = request.FILES.get('image1', None)
        image_wide = request.POST.get('image_wide', False)



        if image1 != None :
            if portfolio.image1 :
                default_storage.delete(portfolio.image1.path)
            portfolio.image1 = image1


        portfolio.index = index
        portfolio.client_name = client_name
        portfolio.client_tagline = client_tagline
        portfolio.services = services
        portfolio.detail = detail
        portfolio.image_wide = image_wide

        portfolio.save()

        msg = "Portfolio has been edited successfully !"
        messages.success(request, msg)

        return redirect('back_portfolio_list')



    try :
        portfolio = Portfolio.objects.get(pk=portfolio_pk)
    except :
        portfolio = None

    if not portfolio :

        msg = "Portfolio not found, try going back and refreshing the page !"
        messages.success(request, msg)

        return redirect('error_back')


    send = {
        'portfolio': portfolio,

    }

    return render(request, 'back/panel/portfolio_edit.html', send)

#< --- [SUB] --- >

def back_portfolio_image_list(request, portfolio_pk) :

    if request.method == 'POST' :

        try :
            portfolio = Portfolio.objects.get(pk=portfolio_pk)
        except :
            portfolio = None

        if not portfolio :
            msg = "Portfolio not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')

        index = request.POST.get('index', None)
        image1 = request.FILES.get('image1', None)

        portfolio_image = Portfolio_Image(
            fk = portfolio,
            index = index,
            image1 = image1,
        )

        portfolio_image.save()

        msg = "Work Image has been added successfully !"
        messages.success(request, msg)

        return redirect('back_portfolio_image_list', portfolio_pk)


    try :
        portfolio = Portfolio.objects.get(pk=portfolio_pk)
    except :
        portfolio = None

    if not portfolio :
        msg = "Portfolio not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    portfolio_image = Portfolio_Image.objects.filter(fk=portfolio)

    index_next = portfolio_image.count() + 1


    send = {
        'portfolio_image': portfolio_image,
        'portfolio_pk': portfolio_pk,
        'index_next': index_next,
    }

    return render(request, 'back/panel/portfolio__image.html', send)



def back_portfolio_image_edit(request, portfolio_pk, portfolio_image_pk) :

    if request.method == 'POST' :

        try :
            portfolio_image = Portfolio_Image.objects.get(pk=portfolio_image_pk)
        except :
            portfolio_image = None

        if not portfolio_image :
            msg = "Portfolio Image not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')


        index = request.POST.get('index', None)
        image1 = request.FILES.get('image1', None)


        if image1 != None :
            if portfolio_image.image1 :
                default_storage.delete(portfolio_image.image1.path)
            portfolio_image.image1 = image1


        portfolio_image.index = index

        portfolio_image.save()

        msg = "Portfolio Work Image has been edited successfully!"
        messages.success(request, msg)

        return redirect('back_portfolio_image_list', portfolio_pk)



    try :
        portfolio_image = Portfolio_Image.objects.get(pk=portfolio_image_pk)
    except :
        portfolio_image = None

    if not portfolio_image :
        msg = "Portfolio Image not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    send = {
        'portfolio_image': portfolio_image,
        'portfolio_pk': portfolio_pk,
    }

    return render(request, 'back/panel/portfolio__image_edit.html', send)



def back_portfolio_image_delete(request, portfolio_pk, portfolio_image_pk) :

    try :
        portfolio_image = Portfolio_Image.objects.get(pk=portfolio_image_pk)
    except :
        portfolio_image = None

    if not portfolio_image :
        msg = "Portfolio Image not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    portfolio_image.delete()

    msg = "Portfolio Work Image has been deleted successfully !"
    messages.success(request, msg)

    return redirect('back_portfolio_image_list', portfolio_pk)





# Service

def back_service_list(request) :

    service = Service.objects.all()


    send = {
        'service': service,
    }

    return render(request, 'back/panel/service_list.html', send)



def back_service_add(request) :

    if request.method == 'POST' :

        service_name = request.POST.get('service_name', '')
        service_intro = request.POST.get('service_intro', '')
        service_detail = request.POST.get('service_detail', '')
        service_list = request.POST.get('service_list', '')

        image1 = request.FILES.get('image1', None)
        image2 = request.FILES.get('image2', None)
        image_before = request.FILES.get('image_before', None)
        image_after = request.FILES.get('image_after', None)

        service_count = Service.objects.all().count()

        index = service_count + 1

        service = Service(
            index = index,
            service_name = service_name,
            service_intro = service_intro,
            service_detail = service_detail,
            service_list = service_list,
            image1 = image1,
            image2 = image2,
            image_before = image_before,
            image_after = image_after,

        )

        service.save()

        msg = "New Service has been listed successfully, now go ahead and add sub-services to it !"
        messages.success(request, msg)

        return redirect('back_service_list')



    return render(request, 'back/panel/service_add.html')



def back_service_edit(request, service_pk) :

    if request.method == 'POST' :

        try :
            service = Service.objects.get(pk=service_pk)
        except :
            service = None

        if not service :
            msg = "Service object not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')

        index = request.POST.get('index', None)
        service_name = request.POST.get('service_name', '')
        service_intro = request.POST.get('service_intro', '')
        service_detail = request.POST.get('service_detail', '')
        service_list = request.POST.get('service_list', '')

        image1 = request.FILES.get('image1', None)
        image2 = request.FILES.get('image2', None)
        image_before = request.FILES.get('image_before', None)
        image_after = request.FILES.get('image_after', None)


        if image1 != None :
            if service.image1 :
                default_storage.delete(service.image1.path)
            service.image1 = image1

        if image2 != None :
            if service.image2 :
                default_storage.delete(service.image2.path)
            service.image2 = image2

        if image_before != None :
            if service.image_before :
                default_storage.delete(service.image_before.path)
            service.image_before = image_before


        if image_after != None :
            if service.image_after :
                default_storage.delete(service.image_after.path)
            service.image_after = image_after


        service.index = index
        service.service_name = service_name
        service.service_intro = service_intro
        service.service_detail = service_detail
        service.service_list = service_list

        service.save()

        msg = "Edits made to " + service.service_name + " has been committed successfully !"
        messages.success(request, msg)

        return redirect('back_service_list')


    try :
        service = Service.objects.get(pk=service_pk)
    except :
        service = None

    if not service :
        msg = "Service object not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')


    send = {
        'service': service,
    }

    return render(request, 'back/panel/service_edit.html', send)



def back_service_delete(request, service_pk) :

    try :
        service = Service.objects.get(pk=service_pk)
    except :
        service = None

    if not service :
        msg = "Service object not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    service.delete()

    msg = "Service has been removed successfully !"
    messages.success(request, msg)

    return redirect('back_service_list')

#< --- [SUB] --- >

def back_service_sub_list(request, service_pk) :

    if request.method == 'POST' :

        try :
            service = Service.objects.get(pk=service_pk)
        except :
            service = None

        if not service :
            msg = "Service object not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')

        index = request.POST.get('index', None)
        name = request.POST.get('name', '')
        tiny_head = request.POST.get('tiny_head', '')
        detail = request.POST.get('detail', '')
        image1 = request.FILES.get('image1', None)

        service_sub = Service_Sub(
            fk = service,
            index = index,
            name = name,
            tiny_head = tiny_head,
            detail = detail,
            image1 = image1,
        )

        service_sub.save()

        msg = "New Sub Service has been added successfully to the " + service.service_name + " !"
        messages.success(request, msg)

        return redirect('back_service_sub_list', service_pk)


    try :
        service = Service.objects.get(pk=service_pk)
    except :
        service = None

    if not service :
        msg = "Service object not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')


    service_sub = Service_Sub.objects.filter(fk=service)

    index_next = service_sub.count() + 1

    send = {
        'service_sub': service_sub,
        'service_pk': service_pk,
        'index_next': index_next,
    }

    return render(request, 'back/panel/service_sub.html', send)



def back_service_sub_edit(request, service_pk, service_sub_pk) :

    if request.method == 'POST' :

        try :
            service_sub = Service_Sub.objects.get(pk=service_sub_pk)
        except :
            service_sub = None

        if not service_sub :
            msg = "Service object not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')

        index =  request.POST.get('index', None)
        name = request.POST.get('name', '')
        tiny_head = request.POST.get('tiny_head', '')
        detail = request.POST.get('detail', '')
        image1 = request.FILES.get('image1', None)

        if image1 != None :
            if service_sub.image1 :
                default_storage.delete(service_sub.image1.path)
            service_sub.image1 = image1

        service_sub.index = index
        service_sub.name = name
        service_sub.tiny_head = tiny_head
        service_sub.detail = detail

        service_sub.save()

        msg = "Edits made to Sub-Service has been committed successfully!"
        messages.success(request, msg)

        return redirect('back_service_sub_list', service_pk)



    try :
        service_sub = Service_Sub.objects.get(pk=service_sub_pk)
    except :
        service_sub = None

    if not service_sub :
        msg = "Service object not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')


    send = {
        'service_sub': service_sub,
        'service_pk': service_pk,
    }

    return render(request, 'back/panel/service_sub_edit.html', send)



def back_service_sub_delete(request, service_pk, service_sub_pk) :

    try :
        service_sub = Service_Sub.objects.get(pk=service_sub_pk)
    except :
        service_sub = None

    if not service_sub :
        msg = "Service object not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    service_sub.delete()

    msg = "Sub service has been removed successfully !"
    messages.success(request, msg)

    return redirect('back_service_sub_list', service_pk)




