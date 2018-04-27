from rest_framework import serializers
from django.utils.translation import gettext as _

from applications.categories.services import get_tree_ads_count
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()
    parent_slug = serializers.SerializerMethodField()
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'slug', 'count', 'parent_slug', 'parent', 'is_leaf_node')

    @classmethod
    def get_count(cls, obj):
        return get_tree_ads_count(obj)

    @classmethod
    def get_parent_slug(cls, obj):
        return obj.parent.slug if obj.parent else 'category'

    @classmethod
    def get_parent(cls, obj):
        return obj.parent.name if obj.parent else _('All rubrics')


