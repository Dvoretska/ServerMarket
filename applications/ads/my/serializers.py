from rest_framework import serializers

from applications.ads.my.models import SavedAd


class SavedAdSerializer(serializers.ModelSerializer):

    class Meta:
        model = SavedAd
        fields = ('ad', 'user')
