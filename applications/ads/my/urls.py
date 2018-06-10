from django.conf.urls import url

from applications.ads.my.views import MyAdsListView, MyAdDetailView, SavedAdView, DeleteSavedAdView, CreateSavedAdView

urlpatterns = [
    url(r'^ads/$', MyAdsListView.as_view(), name='list'),
    url(r'^ads/delete/(?P<slug>[\w-]+)/$', MyAdDetailView.as_view(), name='delete'),
    url(r'^save/(?P<slug>[\w-]+)/$', CreateSavedAdView.as_view(), name='create'),
    url(r'^delete/(?P<slug>[\w-]+)/$', DeleteSavedAdView.as_view(), name='create'),
    url(r'^list/$', SavedAdView.as_view(), name='create'),
]
