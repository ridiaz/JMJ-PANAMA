from django.urls import path
from . import views


from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),
]