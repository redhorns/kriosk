from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Blog, Blog_Section
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain






def home(request):

    return render(request, 'front/home.html')
    

def about(request):

    return render(request, 'front/about.html')


def blog(request):

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

    print("===============")
    for i in similar_blog :
        print(i)

    # next blog
    try :
        current_index = blog_detail.index
        next_index = current_index + 1

        next_blog = Blog.objects.get(index=next_index)
    except :
        next_blog = None


    send = {
        'blog_detail': blog_detail,
        'similar_blog': similar_blog,
        'next_blog': next_blog,
    }

    return render(request, 'front/blog_detail.html', send)


def blog_front_search(request) :

    search = request.GET.get('search', '')

    if search :

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


        send = {
            'section_list': section_list,
            'blog': blog,
            'search': search,
            'count': blogs.count(),
        }

        return render(request, 'front/blog_search.html', send)

    else :
        return HttpResponse("Blog search is broken !")


def blog_filter(request, section_pk) :

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

    send = {
        'section_list': section_list,
        'blog_section': fk_blog_section,
        'blog': blog,
        'count': blogs.count(),
        'first': first,
        'last': last,
    }

    return render(request, 'front/blog.html', send)


def portfolio_list(request):

    return render(request, 'front/portfolio_list.html')


def portfolio_detail(request):

    return render(request, 'front/portfolio_detail.html')


def service_list(request):

    return render(request, 'front/service_list.html')
    

def service_detail(request):

    return render(request, 'front/service_detail.html')


def contact(request):

    return render(request, 'front/contact.html')


def career(request):

    return render(request, 'front/career.html')



def panel(request):

    return render(request, 'back/panel.html')
















