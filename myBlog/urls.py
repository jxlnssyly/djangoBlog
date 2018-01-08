# encoding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(?P<page>\d+)$', views.index),
    url(r'^comment/$',views.comment),
    url(r'^program/$',views.program),
    url(r'^blog/$',views.blog),
    url(r'^detail/(?P<id>[0-9]+)/$',views.detail),
    url(r'^life/$',views.life),
    url(r'^resume/$',views.resume),
    url(r'^mo/$', views.mo),

]