from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from . import views

admin.autodiscover()

urlpatterns = (
    url(r'^$', views.home, name="home"),
    #url(r'^dis/(?P<slug>[\w\-]+)/$', views.medicine_search, name="fredy"),
    # url(r'^serve/$', views.serve, name="serve"),
    url(r'^temp/$', views.checktemp, name="serve"),
)
