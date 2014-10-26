from django.conf.urls import url
from personal_area import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
]