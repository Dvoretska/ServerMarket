from django.conf.urls import url

from applications.ads.my.views import MyAdsListView, MyAdDetailView

urlpatterns = [
    url(r'^ads/$', MyAdsListView.as_view(), name='list'),
    url(r'^ads/delete/(?P<slug>[\w-]+)/$', MyAdDetailView.as_view(), name='delete'),
]
