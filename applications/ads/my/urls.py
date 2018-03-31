from django.conf.urls import url

from applications.ads.my.views import MyAdsListView

urlpatterns = [
    url(r'^ads/$', MyAdsListView.as_view(), name='list'),
]
