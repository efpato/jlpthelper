# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^kanji_analyzer/$', include('jlpthelper.apps.kanji_analyzer.urls')),
    url(r'^tests/$', include('jlpthelper.apps.tests.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.static import static
from jlpthelper import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
