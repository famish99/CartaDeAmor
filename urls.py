from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import CartaDeAmor.views as views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'^create/$', views.CreateView.as_view()),
    )

