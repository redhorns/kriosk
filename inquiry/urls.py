from django.conf.urls import url
from inquiry import views


urlpatterns = [

    url(r'^panel/contact/$', views.contact_back, name='contact_back'),
    url(r'^panel/contact/view/(?P<contact_pk>\d+)/$', views.contact_back_view, name='contact_back_view'),
    url(r'^panel/contact/delete/(?P<contact_pk>\d+)/$', views.contact_back_delete, name='contact_back_delete'),

]
