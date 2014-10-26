from django.conf.urls import url
from django.contrib.auth.views import login, logout
from personal_area import views

urlpatterns = ('',
    url(r'^$', views.register, name='register'),
)