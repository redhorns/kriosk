from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog_Section, Blog
from django.contrib import messages
import datetime
from django.utils.safestring import mark_safe
import json
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain


def blog_list(request):

    blogs = Blog.objects.all().order_by('-index')
    
    page = request.GET.get('page')
    paginator = Paginator(blogs, 5)

    try :
        blog = paginator.page(page)
    except PageNotAnInteger :
        blog = paginator.page(1)
    except EmptyPage :
        blog = paginator.page(paginator.num_pages)


    send = {
        'blog': blog,
        'count': blogs.count(),
    }

    return render(request, 'back/blog/blog_list.html', send)




def blog_add(request):

    if request.method == 'POST':

        section_pk = request.POST.get('section_pk', None)
        title = request.POST.get('title', '')
        intro = request.POST.get('intro', '')
        detail = request.POST.get('detail1', '')
        read_duration = request.POST.get('read_duration', 10)
        tag = request.POST.get('tag', '')
        image1 = request.FILES.get('image1', None)


        # checking : section exists
        try :
            blog_section = Blog_Section.objects.get(pk=section_pk)
        except :
            blog_section = None

        if blog_section == None :

            msg = "Blog Section not found !"
            messages.success(request, msg)

            return redirect('error_back')


        # getting : today's date-time
        today = datetime.datetime.now()
        date = "{} {}, {}".format(today.strftime('%B'), today.day, today.year)


        # checking : read duration
        if not read_duration :
            
            msg = "You must specify Read Duration !"
            messages.success(request, msg)

            return redirect("error_back")


        # indexing : automatic indexing
        last = Blog.objects.last()
        if last :
            index = last.index + 1
        else :
            index = 1


        blog = Blog(

            fk = blog_section,
            index = index,
            title = title,
            intro = intro,
            detail = detail,
            read_duration = read_duration,
            tag = tag,
            date = date,
            image1 = image1,

        )

        blog.save()

        msg = "New Blog has been successfully added to the list!"
        messages.success(request, msg)

        return redirect('blog_list')


    
    blog_section = Blog_Section.objects.all()
    
    send = {
        'blog_section': blog_section,
    }

    return render(request, 'back/blog/blog_add.html', send)




def blog_edit(request, blog_pk) :

    if request.method == 'POST' :

        # checking : if blog exists
        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Blog object not found !"
            messages.success(request, msg)

            return redirect('error_back')

        

        section_pk = request.POST.get('section_pk', None)
        index = request.POST.get('index', '')
        title = request.POST.get('title', '')
        intro = request.POST.get('intro', '')
        detail = request.POST.get('detail1', '')
        read_duration = request.POST.get('read_duration', 10)
        date = request.POST.get('date', '')
        tag = request.POST.get('tag', '')
        image1 = request.FILES.get('image1', None)

        
        # checking : section exists
        try :
            blog_section = Blog_Section.objects.get(pk=section_pk)
        except :
            blog_section = None

        if blog_section == None :

            msg = "Blog Section not found !"
            messages.success(request, msg)

            return redirect('error_back')

        
        # checking : read duration 
        if not index or not read_duration :
            
            msg = "Either Read Duration or index is missing !"
            messages.success(request, msg)

            return redirect("error_back")


        if image1 != None :
            if blog.image1 :
                default_storage.delete(blog.image1.path)
            blog.image1 = image1

        blog.fk = blog_section
        blog.index = index
        blog.title = title
        blog.intro = intro
        blog.detail = detail
        blog.read_duration = read_duration
        blog.date = date
        blog.tag = tag

        blog.save()

        msg = "Voila, Edits made to this blog has been applied successfully !"
        messages.success(request, msg)

        return redirect('blog_list')




    # checking : if blog exists
    try :
        blog = Blog.objects.get(pk=blog_pk)
    except :
        blog = None

    if not blog :

        msg = "Blog object not found !"
        messages.success(request, msg)

        return redirect('error_back')

    if blog.fk :
        blog_section = Blog_Section.objects.all().exclude(pk=blog.fk.pk)
    else :
        blog_section = Blog_Section.objects.all()


    send = {
        'blog': blog,
        'blog_section' : blog_section,
    }

    return render(request, 'back/blog/blog_edit.html', send)




def blog_delete(request, blog_pk) :

    # checking : if blog exists
    try :
        blog = Blog.objects.get(pk=blog_pk)
    except :
        blog = None

    if not blog :

        msg = "Blog object not found !"
        messages.success(request, msg)

        return redirect('error_back')
    
    name = blog.title

    blog.delete()

    msg = "Blog #" + name + " has been successfully deleted !"
    messages.success(request, msg)

    return redirect('blog_list')




def blog_back_search(request) :

    search = request.GET.get('search', '')

    if search :

        blogs = Blog.objects.filter(title__contains=search).order_by("-index")

        paginator = Paginator(blogs, 2)
        page = request.GET.get('page')

        try:
            blog = paginator.get_page(page)
        except PageNotAnInteger:
            blog = paginator.page(1)
        except EmptyPage:
            blog = paginator.page(paginator.num_pages)
        

        send = {
            'blog': blog,
            'search': search,
        }

        return render(request, 'back/blog/blog_search.html', send)

    else :
        return HttpResponse("You're in else section !")




def blog_section_list(request) :

    # fitst()/last() can also work or latest('index')
    blog_section = Blog_Section.objects.all()

    
    send = {
        'blog_section': blog_section,
    }

    return render(request, 'back/blog/blog_section_list.html', send)




def blog_section_add(request) :

    if request.method == 'POST' :

        name = request.POST.get('name', '')

        last = Blog_Section.objects.last()
        if last :
            index = last.index + 1
        else :
            index = 1

        blog_section = Blog_Section(index=index, name=name)
        blog_section.save()

        msg = "New Blog Section #" + name + "has been added successfully!"
        messages.success(request, msg)

        return redirect('blog_section_list')


    blog_section = Blog_Section.objects.all()

    send = {
        'blog_section': blog_section,
    }

    return render(request, 'back/blog/blog_section_list.html', send)




def blog_section_edit(request, section_pk) :

    if request.method == 'POST' :

        try: 
            blog_section = Blog_Section.objects.get(pk=section_pk)
        except :
            blog_section = None

        if blog_section != None :

            name = request.POST.get('name', '')

            blog_section.name = name 
            blog_section.save()

            msg = "Blog section #" + name + " has been updated successfully !"
            messages.success(request, msg)

            return redirect('blog_section_list')

        else :

            msg = "Blog section not found !"
            messages.success(request, msg)

            return redirect('error_back')



    try: 
        blog_section = Blog_Section.objects.get(pk=section_pk)
    except :
        blog_section = None

    if blog_section != None :

        send = {
            'blog_section': blog_section,
        }

        return render(request, 'back/blog/blog_section_edit.html', send)

    else :  

        msg = "Blog section not found !"
        messages.success(request, msg)

        return redirect('error_back')




def blog_section_delete(request, section_pk) :

    try :
        blog_section = Blog_Section.objects.get(pk=section_pk)
    except :
        blog_section = None

    if blog_section != None :

        name = blog_section.name

        blog_section.delete()

        msg = "Blog Section #" + name + " has been successfully deleted !"
        messages.success(request, msg)

        return redirect('blog_section_list')

    else :

        msg = "Blog section not found !"
        messages.success(request, msg)

        return redirect('error_back')

















def temp(request) :

    return render(request, 'temp.html')



def error_back(request) :

    return render(request, 'back/error_back.html')

