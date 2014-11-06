# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.start_kanji, name='start_kanji'),
    url(r'^analyze$', views.send_text),
]
