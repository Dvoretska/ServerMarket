from rest_framework import serializers

from applications.ads.my.models import SavedAd
from applications.ads.serializers import AdListSerializer


class SavedAdSerializer(serializers.ModelSerializer):

    ad = AdListSerializer(read_only=True)

    class Meta:
        model = SavedAd
        fields = ('ad',)


class LightSavedAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedAd
        fields = ('ad', 'user')
