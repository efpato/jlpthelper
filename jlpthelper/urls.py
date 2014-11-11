# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^kanji_analyzer/$', include('jlpthelper.apps.kanji_analyzer.urls')),
)
