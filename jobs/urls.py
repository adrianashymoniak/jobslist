from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<pk>\d+)/$', views.job_details, name='job_details'),
    url(r'^create-job/$', views.create_job, name='create_job'),
    url(r'^delete-all-jobs/$', views.delete_all_jobs, name='delete_all_jobs'),
    url(r'^(?P<pk>\d+)/delete-job/$', views.delete_job, name='delete_job'),
]
