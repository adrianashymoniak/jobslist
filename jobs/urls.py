from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^create/$', views.create_job, name='create_job'),
]
