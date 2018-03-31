from django.conf.urls import url

from applications.ads.views import AdCreateView, AdListView

urlpatterns = [
    url(r'^ad/$', AdCreateView.as_view(), name='create'),
    url(r'^$', AdListView.as_view(), name='list'),
]
