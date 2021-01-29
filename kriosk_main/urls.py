from django.conf.urls import url
from kriosk_main import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog_detail/$', views.blog_detail, name='blog_detail'),
    url(r'^portfolio_list/$', views.portfolio_list, name='portfolio_list'),
    url(r'^portfolio_detail/$', views.portfolio_detail, name='portfolio_detail'),
    url(r'^service_list/$', views.service_list, name='service_list'),
    url(r'^service_detail/$', views.service_detail, name='service_detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^career/$', views.career, name='career'),

    url(r'^panel/$', views.panel, name='panel'),
                     


]





