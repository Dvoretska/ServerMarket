from django.conf.urls import url

from applications.ads.views import CategoriesListView, AdCreateView

urlpatterns = [
    url(r'^categories', CategoriesListView.as_view(), name='get_categories'),
    url(r'^ad', AdCreateView.as_view(), name='post_ad'),
]
