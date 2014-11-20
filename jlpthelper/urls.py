# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^kanji_analyzer/$', include('jlpthelper.apps.kanji_analyzer.urls')),
)
