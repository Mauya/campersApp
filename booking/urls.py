from django.conf.urls import url
from . import views

# Booking form urls
urlpatterns = [
    url(r'^create/$', views.booking_create, name='booking_create'),
    url(r'^(?P<pk>\d+)/$', views.booking_detail, name='booking_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.booking_edit, name='booking_edit'),
    url(r'^$', views.booking_list, name='booking_list'),
    url(r'^(?P<id>\d+)/delete/$', views.booking_delete, name='booking_delete'),
    ]