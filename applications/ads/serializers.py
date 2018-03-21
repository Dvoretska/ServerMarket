from rest_framework import serializers

from applications.ads.models import Category, Ad


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', )


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user')


class AdListSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ('subject', 'message', 'category', 'location', 'user')
