from django.shortcuts import render, redirect
from django.http import HttpResponse
from panel.models import Portfolio, Portfolio_Image, Home, Service_Sub, Service, Page_Handler, Our_Team
from django.contrib import messages
import datetime
from django.utils.safestring import mark_safe
import json
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.contrib.auth.decorators import login_required


# Home

@login_required
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



@login_required
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



@login_required
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

@login_required
def back_portfolio_list(request) :

    portfolio = Portfolio.objects.all().order_by('index')

    send = {
        'portfolio': portfolio,

    }

    return render(request, 'back/panel/portfolio_list.html', send)



@login_required
def back_portfolio_add(request) :

    if request.method == 'POST' :

        client_name = request.POST.get('client_name', '')
        client_tagline = request.POST.get('client_tagline', '')
        detail = request.POST.get('detail1', '')

        service_advt_bool = request.POST.get('service_advt_bool', False)
        service_advt = request.POST.get('service_advt', '')
        service_bi_bool = request.POST.get('service_bi_bool', False)
        service_bi = request.POST.get('service_bi', '')
        service_digital_bool = request.POST.get('service_digital_bool', False)
        service_digital = request.POST.get('service_digital', '')

        image1 = request.FILES.get('image1', None)
        image_wide = request.POST.get('image_wide', None)

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        # auto indexing
        index = Portfolio.objects.all().count() + 1

        # checking : image is wide
        # if image_wide :
        #     image_wide = image_wide
        # else :
        #     image_wide = False

        portfolio = Portfolio(
            index = index,
            client_name = client_name,
            client_tagline = client_tagline,
            detail = detail,

            service_advt_bool = service_advt_bool,
            service_advt = service_advt,
            service_bi_bool = service_bi_bool,
            service_bi = service_bi,
            service_digital_bool = service_digital_bool,
            service_digital = service_digital,

            image1 = image1,
            image_wide = image_wide,

            meta_title = meta_title,
            meta_description = meta_description,
        )

        portfolio.save()

        msg = "New client portfolio has been added successfully !"
        messages.success(request, msg)

        return redirect('back_portfolio_list')



    return render(request, 'back/panel/portfolio_add.html')



@login_required
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
        detail = request.POST.get('detail1', '')

        service_advt_bool = request.POST.get('service_advt_bool', False)
        service_advt = request.POST.get('service_advt', '')
        service_bi_bool = request.POST.get('service_bi_bool', False)
        service_bi = request.POST.get('service_bi', '')
        service_digital_bool = request.POST.get('service_digital_bool', False)
        service_digital = request.POST.get('service_digital', '')

        image1 = request.FILES.get('image1', None)
        image_wide = request.POST.get('image_wide', False)

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')



        if image1 != None :
            if portfolio.image1 :
                default_storage.delete(portfolio.image1.path)
            portfolio.image1 = image1


        portfolio.index = index
        portfolio.client_name = client_name
        portfolio.client_tagline = client_tagline
        portfolio.detail = detail

        portfolio.service_advt_bool = service_advt_bool
        portfolio.service_advt = service_advt
        portfolio.service_bi_bool = service_bi_bool
        portfolio.service_bi = service_bi
        portfolio.service_digital_bool = service_digital_bool
        portfolio.service_digital = service_digital

        portfolio.image_wide = image_wide

        portfolio. meta_title = meta_title
        portfolio.meta_description = meta_description

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

@login_required
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

    portfolio_image = Portfolio_Image.objects.filter(fk=portfolio).order_by('index')

    index_next = portfolio_image.count() + 1

    send = {
        'portfolio_image': portfolio_image,
        'portfolio_pk': portfolio_pk,
        'index_next': index_next,
    }

    return render(request, 'back/panel/portfolio__image.html', send)



@login_required
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



@login_required
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

@login_required
def back_service_list(request) :

    service = Service.objects.all().order_by('index')


    send = {
        'service': service,
    }

    return render(request, 'back/panel/service_list.html', send)



@login_required
def back_service_add(request) :

    if request.method == 'POST' :

        service_name = request.POST.get('service_name', '')
        service_inner = request.POST.get('service_inner', '')
        service_intro = request.POST.get('service_intro', '')
        service_detail = request.POST.get('service_detail', '')

        image1 = request.FILES.get('image1', None)
        image2 = request.FILES.get('image2', None)
        image_before = request.FILES.get('image_before', None)
        image_after = request.FILES.get('image_after', None)

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        service_count = Service.objects.all().count()

        index = service_count + 1

        service = Service(
            index = index,
            service_name = service_name,
            service_inner = service_inner,
            service_intro = service_intro,
            service_detail = service_detail,
            image1 = image1,
            image2 = image2,
            image_before = image_before,
            image_after = image_after,
            meta_title = meta_title,
            meta_description = meta_description,

        )

        service.save()

        msg = "New Service has been listed successfully, now go ahead and add sub-services to it !"
        messages.success(request, msg)

        return redirect('back_service_list')



    return render(request, 'back/panel/service_add.html')



@login_required
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
        service_inner = request.POST.get('service_inner', '')
        service_intro = request.POST.get('service_intro', '')
        service_detail = request.POST.get('service_detail', '')

        image1 = request.FILES.get('image1', None)
        image2 = request.FILES.get('image2', None)
        image_before = request.FILES.get('image_before', None)
        image_after = request.FILES.get('image_after', None)

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')


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
        service.service_inner = service_inner
        service.service_intro = service_intro
        service.service_detail = service_detail

        service.meta_title = meta_title
        service.meta_description = meta_description

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



@login_required
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

@login_required
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


    service_sub = Service_Sub.objects.filter(fk=service).order_by('index')

    index_next = service_sub.count() + 1

    send = {
        'service_sub': service_sub,
        'service_pk': service_pk,
        'index_next': index_next,
    }

    return render(request, 'back/panel/service_sub.html', send)



@login_required
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



@login_required
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



# Meta

@login_required
def page_list(request) :

    page_handler = Page_Handler.objects.all()

    send = {
        'page_handler' : page_handler,
    }

    return render(request, 'back/panel/page_list.html', send)



@login_required
def page_add(request) :

    if request.method == 'POST' :

        page_name = request.POST.get('page_name', '')
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        page_handler = Page_Handler (
            page_name = page_name,
            meta_title = meta_title,
            meta_description = meta_description,
        )

        page_handler.save()

        msg = "New Page has been added to Page-List"
        messages.success(request, msg)

        return redirect('page_list')

    return render(request, 'back/panel/page_add.html')



@login_required
def page_edit(request, page_pk) :

    if request.method == 'POST' :

        try :
            page_handler = Page_Handler.objects.get(pk=page_pk)
        except :
            page_handler = None

        if not page_handler :
            msg = "Page not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')

        page_name = request.POST.get('page_name', '')
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        page_handler.page_name = page_name
        page_handler.meta_title = meta_title
        page_handler.meta_description = meta_description

        page_handler.save()

        msg = "Edits made to Page has been committed successfully !"
        messages.success(request, msg)

        return redirect('page_list')


    try :
        page_handler = Page_Handler.objects.get(pk=page_pk)
    except :
        page_handler = None

    if not page_handler :
        msg = "Page not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    send = {
        'page_handler': page_handler,
    }

    return render(request, 'back/panel/page_edit.html', send)


# team

@login_required
def team_list(request) :

    our_team = Our_Team.objects.all().order_by('index')

    send = {
        'our_team': our_team,
    }

    return render(request, 'back/panel/our_team_list.html', send)



@login_required
def team_add(request) :

    if request.method == 'POST':

        index = request.POST.get('index', '')
        name = request.POST.get('name', '')
        intro = request.POST.get('intro', '')
        desg = request.POST.get('desg', '')

        image1 = request.FILES.get('image1', None)
        our_team = Our_Team(
            index = index,
            name = name,
            intro = intro,
            desg = desg,
            image1 = image1,
        )

        our_team.save()

        msg = "New member has been successfully added to the team !"
        messages.success(request, msg)

        return redirect('team_list')


    return render(request, 'back/panel/our_team_add.html')



@login_required
def team_edit(request, team_pk) :

    if request.method == 'POST' :

        try :
            our_team = Our_Team.objects.get(pk=team_pk)
        except :
            our_team = None

        if not our_team :
            msg = "Page not found, try going back, refresh the page and try again !"
            messages.success(request, msg)

            return redirect('error_back')

        index = request.POST.get('index', '')
        name = request.POST.get('name', '')
        intro = request.POST.get('intro', '')
        desg = request.POST.get('desg', '')

        image1 = request.FILES.get('image1', None)

        if image1 != None :
            if our_team.image1 :
                default_storage.delete(our_team.image1.path)
            our_team.image1 = image1

        our_team.index = index
        our_team.name = name
        our_team.intro = intro
        our_team.desg = desg

        our_team.save()

        msg = "Changes made to Team Member has been committed successfully !"
        messages.success(request, msg)
        

        return redirect('team_list')


    
    try :
        our_team = Our_Team.objects.get(pk=team_pk)
    except :
        our_team = None

    if not our_team :
        msg = "Page not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    send = {
        'our_team': our_team,
    }

    return render(request, 'back/panel/our_team_edit.html', send)



@login_required
def team_delete(request, team_pk) :

    try :
        our_team = Our_Team.objects.get(pk=team_pk)
    except :
        our_team = None

    if not our_team :
        msg = "Page not found, try going back, refresh the page and try again !"
        messages.success(request, msg)

        return redirect('error_back')

    our_team.delete()

    msg = "Team Member has been removed successfully !"
    messages.success(request, msg)

    return redirect('team_list')
