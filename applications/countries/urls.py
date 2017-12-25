from django.conf.urls import url

from applications.countries.views import CountryView

urlpatterns = [
    url(r'^', CountryView.as_view(), name='account_signup'),
]
