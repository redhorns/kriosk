from django.conf.urls import url
from inquiry import views


urlpatterns = [

    url(r'^panel/contact/$', views.contact_back, name='contact_back'),
    url(r'^panel/contact/view/(?P<contact_pk>\d+)/$', views.contact_back_view, name='contact_back_view'),
    url(r'^panel/contact/delete/(?P<contact_pk>\d+)/$', views.contact_back_delete, name='contact_back_delete'),

    url(r'^panel/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^panel/newsletter/list/$', views.newsletter_list, name='newsletter_list'),
    url(r'^panel/newsletter/delete/(?P<newsletter_pk>\d+)/$', views.newsletter_delete, name='newsletter_delete'),

    url(r'^panel/career/list/$', views.career_list, name='career_list'),
    url(r'^panel/career/add/$', views.career_add, name='career_add'),
    url(r'^panel/career/edit/(?P<career_pk>\d+)/$', views.career_edit, name='career_edit'),
    url(r'^panel/career/delete/(?P<career_pk>\d+)/$', views.career_delete, name='career_delete'),

    url(r'^panel/career/applicants/list/$', views.applicants_list, name='applicants_list'),
    url(r'^panel/career/applicants/delete/(?P<app_pk>\d+)/$', views.applicants_delete, name='applicants_delete'),

    url(r'^panel/free-trial/list/$', views.free_trial, name='free_trial'),
    url(r'^panel/free-trial/delete/(?P<free_pk>\d+)/$', views.free_trial_delete, name='free_trial_delete'),

]
