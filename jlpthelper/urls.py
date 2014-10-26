from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
    url(r'^kanji_analyzer/', include('kanji_analyzer.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', include('personal_area.urls')),
)