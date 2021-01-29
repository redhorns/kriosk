from django.conf.urls import url
from blog import views


urlpatterns = [

    url(r'^panel/blog/list/$', views.blog_list, name='blog_list'),
    url(r'^panel/blog/add/$', views.blog_add, name='blog_add'),
    url(r'^panel/blog/edit/(?P<blog_pk>\d+)/$', views.blog_edit, name='blog_edit'),
    url(r'^panel/blog/delete/(?P<blog_pk>\d+)/$', views.blog_delete, name='blog_delete'),



    url(r'^panel/blog_section/list/$', views.blog_section_list, name='blog_section_list'),
    url(r'^panel/blog_section/add/$', views.blog_section_add, name='blog_section_add'),
    url(r'^panel/blog_section/edit/(?P<section_pk>\d+)/$', views.blog_section_edit, name='blog_section_edit'),
    url(r'^panel/blog_section/delete/(?P<section_pk>\d+)/$', views.blog_section_delete, name='blog_section_delete'),



    url(r'^panel/temp/$', views.temp, name='temp'),
    url(r'^panel/error/$', views.error_back, name='error_back'),


]





