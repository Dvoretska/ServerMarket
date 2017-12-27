from django.conf.urls import url

from applications.location.views import CountryView, CitiesView

urlpatterns = [
    url(r'^countries/', CountryView.as_view(), name='countries'),
    url(r'^(?P<code>[-:\w]+)/cities/$', CitiesView.as_view(), name='cities'),
]
