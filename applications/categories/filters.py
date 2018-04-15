from django_filters import rest_framework as filters, Filter

from applications.categories.models import Category


class CategoryFilter(filters.FilterSet):

    category = Filter(field_name='parent__slug')

    class Meta:
        model = Category
        fields = ('category', )
