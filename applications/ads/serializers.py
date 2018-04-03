from rest_framework import serializers

from applications.ads.models import Ad
from applications.categories.serializers import CategorySerializer

from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user', 'price', 'image')


class AdListSerializer(CachedSerializerMixin, serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Ad


cache_registry.register(AdListSerializer)
