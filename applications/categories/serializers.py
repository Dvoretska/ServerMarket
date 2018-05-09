from django.db.models import Q
from rest_framework import serializers
from django.utils.translation import gettext as _
from rest_framework_cache.registry import cache_registry

from applications.categories.services import get_tree_ads_count
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()
    parent_slug = serializers.SerializerMethodField()
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'slug', 'count', 'parent_slug', 'parent', 'is_leaf_node')

    def get_count(self, obj):
        min_price = self.context['request'].query_params.get('min_price')
        max_price = self.context['request'].query_params.get('max_price')
        return get_tree_ads_count(
            obj,
            Q(price__gte=min_price) if min_price else Q(),
            Q(price__lte=max_price) if min_price else Q()
        )

    @classmethod
    def get_parent_slug(cls, obj):
        return obj.parent.slug if obj.parent else 'category'

    @classmethod
    def get_parent(cls, obj):
        return obj.parent.name if obj.parent else _('All rubrics')


cache_registry.register(CategorySerializer)
