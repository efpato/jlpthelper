from django.conf.urls import url
from kanji_analyzer import views

urlpatterns = [
    url(r'^$', views.start_kanji, name='start_kanji'),
    url(r'^analyze$', views.send_text),
]