from django.conf.urls import url

from applications.countries.views import CountryView, CitiesView

urlpatterns = [
    url(r'^(?P<code>[-:\w]+)$', CitiesView.as_view(), name='cities'),
    url(r'^', CountryView.as_view(), name='countries'),
]
