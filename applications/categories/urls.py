from django.conf.urls import url

from applications.categories.views import CategoriesListView

urlpatterns = [
    url(r'^$', CategoriesListView.as_view(), name='get_categories'),
]
