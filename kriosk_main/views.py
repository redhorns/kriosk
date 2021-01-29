from django.shortcuts import render, redirect
from django.http import HttpResponse






def home(request):

    return render(request, 'front/home.html')
    

def about(request):

    return render(request, 'front/about.html')


def blog(request):

    return render(request, 'front/blog.html')


def blog_detail(request):

    return render(request, 'front/blog_detail.html')


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
















