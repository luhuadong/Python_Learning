from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^monitor/$', views.index, name='index'),
    url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),
]