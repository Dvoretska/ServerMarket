from rest_framework import serializers

from applications.accounts import models


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = 'last_name', 'first_name', 'country', 'city', 'username', 'email'
