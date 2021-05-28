from django.conf.urls import url
from panel import views


urlpatterns = [

    url(r'^panel/home/list/$', views.home_back, name='home_back'),
    url(r'^panel/home/edit/(?P<home_pk>\d+)/$', views.home_edit_back, name='home_edit_back'),
    url(r'^panel/home/delete/(?P<home_pk>\d+)/$', views.home_delete_back, name='home_delete_back'),

    # portfolio
    url(r'^panel/portfolio/list/$', views.back_portfolio_list, name='back_portfolio_list'),
    url(r'^panel/portfolio/add/$', views.back_portfolio_add, name='back_portfolio_add'),
    url(r'^panel/portfolio/edit/(?P<portfolio_pk>\d+)/$', views.back_portfolio_edit, name='back_portfolio_edit'),

    url(r'^panel/portfolio/image/list/(?P<portfolio_pk>\d+)/$', views.back_portfolio_image_list, name='back_portfolio_image_list'),
    url(r'^panel/portfolio/image/edit/(?P<portfolio_pk>\d+)/(?P<portfolio_image_pk>\d+)/$', views.back_portfolio_image_edit, name='back_portfolio_image_edit'),
    url(r'^panel/portfolio/image/delete/(?P<portfolio_pk>\d+)/(?P<portfolio_image_pk>\d+)/$', views.back_portfolio_image_delete, name='back_portfolio_image_delete'),

    # service
    url(r'^panel/service/list/$', views.back_service_list, name='back_service_list'),
    url(r'^panel/service/add/$', views.back_service_add, name='back_service_add'),
    url(r'^panel/service/edit/(?P<service_pk>\d+)/$', views.back_service_edit, name='back_service_edit'),
    url(r'^panel/service/delete/(?P<service_pk>\d+)/$', views.back_service_delete, name='back_service_delete'),

    url(r'^panel/service/sub/list/(?P<service_pk>\d+)/$', views.back_service_sub_list, name='back_service_sub_list'),
    url(r'^panel/service/sub/edit/(?P<service_pk>\d+)/(?P<service_sub_pk>\d+)/$', views.back_service_sub_edit, name='back_service_sub_edit'),
    url(r'^panel/service/sub/delete/(?P<service_pk>\d+)/(?P<service_sub_pk>\d+)/$', views.back_service_sub_delete, name='back_service_sub_delete'),

    # page (meta)
    url(r'^panel/page/list/$', views.page_list, name='page_list'),
    url(r'^panel/page/add/$', views.page_add, name='page_add'),
    url(r'^panel/page/edit/(?P<page_pk>\d+)/$', views.page_edit, name='page_edit'),

    # team
    url(r'^panel/team/list/$', views.team_list, name='team_list'),
    url(r'^panel/team/add/$', views.team_add, name='team_add'),
    url(r'^panel/team/edit/(?P<team_pk>\d+)/$', views.team_edit, name='team_edit'),
    url(r'^panel/team/delete/(?P<team_pk>\d+)/$', views.team_delete, name='team_delete'),


]
