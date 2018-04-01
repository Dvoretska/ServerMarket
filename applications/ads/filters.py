from django_filters import rest_framework as filters

from applications.ads.models import Ad


class AdFilter(filters.FilterSet):

    category = filters.CharFilter(field_name='category__name')

    class Meta:
        model = Ad
        fields = ('category', )
