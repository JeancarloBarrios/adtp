from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()

urlpatterns = (
    url(r'^$', views.home, name="home"),
    #url(r'^dis/(?P<slug>[\w\-]+)/$', views.medicine_search, name="fredy"),
    url(r'^servo/$', views.servo, name="servo"),
    url(r'^temp/$', views.checktemp, name="temp"),
    url(r'^save/$', views.save, name="save"),
    url(r'^show/$', views.show, name="show"),

)
