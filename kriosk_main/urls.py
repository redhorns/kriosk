from django.conf.urls import url
from kriosk_main import views


urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

    # blog
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<blog_slug>.*)/$', views.blog_detail, name='blog_detail'),
    url(r'^blog/search/$', views.blog_front_search, name='blog_front_search'),
    url(r'^blog/filter/(?P<section_pk>\d+)/$', views.blog_filter, name='blog_filter'),


    url(r'^portfolio/$', views.portfolio_list, name='portfolio_list'),
    url(r'^portfolio/(?P<portfolio_name_slug>.*)/$', views.portfolio_detail, name='portfolio_detail'),

    url(r'^service/$', views.service_list, name='service_list'),
    url(r'^service/(?P<service_name_slug>.*)/$', views.service_detail, name='service_detail'),
    
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^career/$', views.career, name='career'),

    url(r'^panel/$', views.panel, name='panel'),

                     


]





