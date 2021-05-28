from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Blog, Blog_Section
from panel.models import Home, Portfolio, Portfolio_Image, Service, Service_Sub, Page_Handler, Our_Team
from inquiry.models import Career, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from django.contrib.auth.decorators import login_required





# < ============================== Home ============================== >

def home(request):

    home = Home.objects.all()

    services = Service.objects.all()

    try :
        page_handler = Page_Handler.objects.get(pk=1)
    except :
        page_handler = None



    send = {
        'home': home,
        'services': services,
        'page_handler': page_handler,
    }

    return render(request, 'front/home.html', send)
    

# < ============================== About ============================== >

def about(request):

    try :
        page_handler = Page_Handler.objects.get(pk=2)
    except :
        page_handler = None

    services = Service.objects.all()

    blog = Blog.objects.last()

    blogs = Blog.objects.all().exclude(pk=blog.pk).order_by('-pk')[:3]

    our_team = Our_Team.objects.all().order_by('index')


    send = {
        'page_handler': page_handler,
        'services': services,
        'blog': blog,
        'blogs': blogs,
        'our_team': our_team,
    }

    return render(request, 'front/about.html', send)


# < ==============================  Blog  ============================= >

def blog(request):

    try :
        page_handler = Page_Handler.objects.get(pk=5)
    except :
        page_handler = None

    services = Service.objects.all()

    blog_section = Blog_Section.objects.all()
    section_list = []

    for i in blog_section :
        count = Blog.objects.filter(fk=i).count()
        mytuple = (count, i)
        section_list.append(mytuple)


    blogs = Blog.objects.all().order_by('-index')

    # paginator
    page = request.GET.get('page')
    paginator = Paginator(blogs, 8)

    try :
        blog = paginator.page(page)
    except PageNotAnInteger : 
        blog = paginator.page(1)
    except EmptyPage :
        blog = paginator.page(paginator.num_pages)

    
    # i.e. Showing 5-8 of 6 results
    first, last = 1, 8
    if page :
        try :
            first = 1 + ((int(page) - 1) * 8)
            last = int(page) * 8
        except :
            return HttpResponse("error")


    send = {
        'page_handler': page_handler,
        'services': services,
        'section_list': section_list,
        'blog': blog,
        'count': blogs.count(),
        'first': first,
        'last': last,
    }

    return render(request, 'front/blog.html', send)


def blog_detail(request, blog_slug):

    # blog
    try :
        blog_detail = Blog.objects.get(title_slug=blog_slug)
    except :
        return HttpResponse("You are nowhere, Blog not found !")

    # similar blogs
    try :
        similar_blog = Blog.objects.filter(fk=blog_detail.fk).exclude(pk=blog_detail.pk).order_by("-index")[1:4]
    except :
        similar_blog = None

    # next blog
    try :
        current_index = blog_detail.index
        next_index = current_index - 1

        next_blog = Blog.objects.get(index=next_index)
    except :
        next_blog = None

    # prev blog
    try :
        current_index = blog_detail.index
        prev_index = current_index + 1

        prev_blog = Blog.objects.get(index=prev_index)
    except :
        prev_blog = None

    tags_raw = blog_detail.tag
    tags = tags_raw.split(',')

    services = Service.objects.all()


    send = {
        'services': services,
        'blog_detail': blog_detail,
        'similar_blog': similar_blog,
        'next_blog': next_blog,
        'prev_blog': prev_blog,
        'tags': tags,
    }

    return render(request, 'front/blog_detail.html', send)


def blog_front_search(request) :

    search = request.GET.get('search', '')

    if search :

        try :
            page_handler = Page_Handler.objects.get(pk=5)
        except :
            page_handler = None

        # blog categories
        blog_section = Blog_Section.objects.all()
        section_list = []

        for i in blog_section :
            count = Blog.objects.filter(fk=i).count()
            mytuple = (count, i)
            section_list.append(mytuple)

        # getting : blogs matching recieved Search Keyword
        blogs = Blog.objects.filter(title__contains=search).order_by("-index")

        # pagination
        page = request.GET.get('page')
        paginator = Paginator(blogs, 8)

        try :
            blog = paginator.page(page)
        except PageNotAnInteger : 
            blog = paginator.page(1)
        except EmptyPage :
            blog = paginator.page(paginator.num_pages)

        services = Service.objects.all()


        send = {
            'services': services,
            'page_handler': page_handler,
            'section_list': section_list,
            'blog': blog,
            'search': search,
            'count': blogs.count(),
        }

        return render(request, 'front/blog_search.html', send)

    else :
        return HttpResponse("Blog search is broken !")


def blog_filter(request, section_pk) :

    try :
        page_handler = Page_Handler.objects.get(pk=5)
    except :
        page_handler = None

    # blog categories
    blog_section = Blog_Section.objects.all()
    section_list = []

    for i in blog_section :
        count = Blog.objects.filter(fk=i).count()
        mytuple = (count, i)
        section_list.append(mytuple)

    # getting : blog_section matching recieved section_pk
    try :
        fk_blog_section = Blog_Section.objects.get(pk=section_pk)
    except :
        return HttpResponse("You are nowhere, Blog Section not found whilte Filtering Blog !")
    
    blogs = Blog.objects.filter(fk=fk_blog_section).order_by('-index')

    # paginator
    page = request.GET.get('page')
    paginator = Paginator(blogs, 8)

    try :
        blog = paginator.page(page)
    except PageNotAnInteger : 
        blog = paginator.page(1)
    except EmptyPage :
        blog = paginator.page(paginator.num_pages)

    
    # i.e. Showing 5-8 of 6 results
    first, last = 1, 8
    if page :
        try :
            first = 1 + ((int(page) - 1) * 8)
            last = int(page) * 8
        except :
            return HttpResponse("error")

    services = Service.objects.all()

    send = {
        'services': services,
        'page_handler': page_handler,
        'section_list': section_list,
        'blog_section': fk_blog_section,
        'blog': blog,
        'count': blogs.count(),
        'first': first,
        'last': last,
    }

    return render(request, 'front/blog.html', send)



# < ============================  Portfolio  =========================== >

def portfolio_list(request):

    services = Service.objects.all()

    try :
        page_handler = Page_Handler.objects.get(pk=3)
    except :
        page_handler = None

    portfolios = Portfolio.objects.all().order_by('index')

    send = {
        'page_handler': page_handler,
        'portfolios': portfolios,
        'services': services,
    }

    return render(request, 'front/portfolio_list.html', send)


def portfolio_detail(request, portfolio_name_slug):

    services = Service.objects.all()

    try :
        portfolio = Portfolio.objects.get(client_name_slug=portfolio_name_slug)
    except :
        portfolio = None

    if portfolio == None :
        return HttpResponse("You are nowhere, Portfolio not found !")
    

    portfolio_images = Portfolio_Image.objects.filter(fk=portfolio).order_by('index')

    # next portfolio
    try :
        current_index = portfolio.index
        next_index = current_index + 1

        next_portfolio = Portfolio.objects.get(index=next_index)
    except :
        next_portfolio = None

    # prev portfolio
    try :
        current_index = portfolio.index
        prev_index = current_index - 1

        prev_portfolio = Portfolio.objects.get(index=prev_index)
    except :
        prev_portfolio = None
    
    send = {
        'portfolio': portfolio,
        'portfolio_images': portfolio_images,
        'next_portfolio': next_portfolio,
        'prev_portfolio': prev_portfolio,
        'services': services,
    }

    return render(request, 'front/portfolio_detail.html', send)



# < ===========================  Service  ============================== >

def service_list(request):

    try :
        page_handler = Page_Handler.objects.get(pk=4)
    except :
        page_handler = None


    services = Service.objects.all().order_by('index')


    send = {
        'page_handler': page_handler,
        'services': services,
    }

    return render(request, 'front/service_list.html', send)
    

def service_detail(request, service_name_slug):

    services = Service.objects.all()

    try :
        service = Service.objects.get(service_name_slug=service_name_slug)
    except :
        service = None

    if not service :
        return HttpResponse("Service not found !")

    service_sub = Service_Sub.objects.filter(fk=service).order_by('index')

    # next service
    try :
        current_index = service.index
        next_index = current_index + 1

        next_service = Service.objects.get(index=next_index)
    except :
        next_service = None

    # prev service
    try :
        current_index = service.index
        prev_index = current_index - 1

        prev_service = Service.objects.get(index=prev_index)
    except :
        prev_service = None

    send = {
        'services': services,
        'service': service,
        'service_sub': service_sub,
        'next_service': next_service,
        'prev_service': prev_service,
    }

    return render(request, 'front/service_detail.html', send)


# < ===========================  Contact  =============================== >

def contact(request):

    services = Service.objects.all()

    try :
        page_handler = Page_Handler.objects.get(pk=6)
    except :
        page_handler = None

    send = {
        'page_handler': page_handler,
        'services': services,
    }

    return render(request, 'front/contact.html', send)


# < ==========================  Career  ================================= >

def career(request):

    try :
        page_handler = Page_Handler.objects.get(pk=7)
    except :
        page_handler = None

    services = Service.objects.all()

    career = Career.objects.all().exclude(status=False)
    career_all = Career.objects.all()
    

    send = {
        'page_handler': page_handler,
        'services': services,
        'career': career,
        'career_all': career_all,
    }

    return render(request, 'front/career.html', send)


@login_required
def panel(request):

    contact = Contact.objects.all().order_by('-pk')[0:5]


    blog_count = Blog.objects.all().count()

    if blog_count % 10 == 1 :
        blog_count = str(blog_count) + 'st'
    elif blog_count % 10 == 2 :
        blog_count = str(blog_count) + 'nd'
    elif blog_count % 10 == 3 :
        blog_count = str(blog_count) + 'rd'
    else :
        blog_count = str(blog_count) + 'th'

    send = {
        'contact': contact,
        'blog_count': blog_count,
    }

    return render(request, 'back/panel.html', send)















