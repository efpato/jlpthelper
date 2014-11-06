# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^kanji_analyzer/', include('jlpthelper.apps.kanji_analyzer.urls')),
    url(r'^site_auth/', include('site_auth.urls')),
    url(r'^admin/', include(admin.site.urls))
)
