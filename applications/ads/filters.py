from django_filters import rest_framework as filters

from applications.ads.models import Ad

from django_filters import Filter
from django_filters.fields import Lookup


class ListFilter(Filter):
    def filter(self, qs, value):
        return super().filter(qs, Lookup(value.split(','), 'in'))


class AdFilter(filters.FilterSet):

    category = ListFilter(field_name='category__slug')

    class Meta:
        model = Ad
        fields = ('category', )
