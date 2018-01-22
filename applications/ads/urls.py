from django.conf.urls import url

from applications.ads.views import CategoriesView

urlpatterns = [
    url(r'^categories', CategoriesView.as_view(), name='get_categories'),
]
