from django.conf.urls import url

from applications.ads.views import AdCreateView, AdListView, AdDetailView

urlpatterns = [
    url(r'^ad/$', AdCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', AdDetailView.as_view(), name='detail'),
    url(r'^$', AdListView.as_view(), name='list')
]
