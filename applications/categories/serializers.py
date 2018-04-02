from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('name', 'slug', 'count')

    @classmethod
    def get_count(cls, obj):
        return obj.categories.count()

