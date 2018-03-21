from django.conf.urls import url

from applications.ads.views import CategoriesListView, AdCreateView, AdListView

urlpatterns = [
    url(r'^categories/$', CategoriesListView.as_view(), name='get_categories'),
    url(r'^ad/$', AdCreateView.as_view(), name='create'),
    url(r'^$', AdListView.as_view(), name='list'),
]
