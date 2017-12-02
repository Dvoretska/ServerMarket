from rest_framework import serializers

from accounts import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('last_name', 'first_name')
