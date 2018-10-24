from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_host_stat', views.get_host_stat, name='getHostStat'),
]