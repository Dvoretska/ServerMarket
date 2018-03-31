from rest_framework import serializers

from applications.ads.models import Ad
from applications.categories.serializers import CategorySerializer


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user', 'price', 'image')


class AdListSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user', 'price', 'image')
