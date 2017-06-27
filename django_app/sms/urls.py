from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.sms_send, name='sms_send'),
    # url(r'^ok/$', views.ok, name='sms_send_ok')
]