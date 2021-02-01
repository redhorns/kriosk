from django.conf.urls import url, include
from authentication import views


urlpatterns = [

    url(r"^authentication/register/$", views.myregister, name="myregister"),
    url(r"^authentication/activation_initiate/$", views.myactivation_initiate, name="myactivation_initiate"),
    url(r"^authentication/activation_end/$", views.myactivation_end, name="myactivation_end"),
    url(r"^authentication/login/$", views.mylogin, name="mylogin"),
    url(r"^authentication/logout/$", views.mylogout, name="mylogout"),


]
