from django_filters import rest_framework as filters, Filter
from django_filters.fields import Lookup

from applications.categories.models import Category


class ListFilter(Filter):
    def filter(self, qs, value):
        return super().filter(qs, Lookup([value.split(',')[0]], 'in'))


class CategoryFilter(filters.FilterSet):

    category = ListFilter(field_name='parent__slug')

    class Meta:
        model = Category
        fields = ('category', )
