from django.conf.urls import patterns, url

from landingpage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

