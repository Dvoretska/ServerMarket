from django.conf.urls import url

from applications.ads.views import CategoriesListView, AdCreateView, AdListView

urlpatterns = [
    url(r'^$', CategoriesListView.as_view(), name='get_categories'),
]
