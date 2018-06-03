from django_filters import rest_framework as filters, OrderingFilter

from applications.ads.models import Ad

from django_filters import Filter, NumberFilter
from django_filters.fields import Lookup

from applications.categories.services import get_flat_tree_categories_list, is_category_exists


class ListFilter(Filter):
    def filter(self, qs, value):
        return super().filter(qs, Lookup(self.get_lookups(value), 'in'))

    @classmethod
    def get_lookups(cls, value):
        lookups = []
        for category in value.split(','):
            if is_category_exists(category):
                lookups.extend([category] + get_flat_tree_categories_list(category))
        return lookups


class AdFilter(filters.FilterSet):

    category = ListFilter(field_name='category__slug')
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Ad
        fields = ('category', 'min_price', 'max_price')
