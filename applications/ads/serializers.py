from rest_framework import serializers

from applications.ads.models import Ad
from applications.categories.serializers import CategorySerializer

from rest_framework_cache.serializers import CachedSerializerMixin
from rest_framework_cache.registry import cache_registry


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user', 'price', 'pk')


class AdListSerializer(CachedSerializerMixin, serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ('slug', 'subject', 'message', 'category', 'location', 'user', 'price', 'image', 'created')

    @classmethod
    def get_image(cls, obj):
        image_instance = obj.images.first()
        if image_instance:
            return image_instance.image.url


class AdDetailSerializer(CachedSerializerMixin, serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user', 'price', 'images', 'created')

    def get_images(self, obj):
        return [ad_image.image.url for ad_image in obj.images.all()]


cache_registry.register(AdListSerializer)
