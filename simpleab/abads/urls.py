from django.conf.urls import patterns, url

from abads import views

urlpatterns = patterns('',
    url(r'^get_ad/(?P<exp_id>\d+)','abads.views.get_ad'),
    url(r'^click/(?P<exp_id>\d+)','abads.views.record_click'),
    url(r'^test','abads.views.test'),
    
)