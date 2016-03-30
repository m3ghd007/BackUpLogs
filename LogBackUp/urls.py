from django.conf.urls import url

from . import views, logs_rest
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getlogs$', logs_rest.get_downloaded_logs, name='getlogs'),
]

urlpatterns += staticfiles_urlpatterns()
