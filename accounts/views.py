from rest_framework import generics
from rest_framework import mixins

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer


class UserProfileView(mixins.UpdateModelMixin, generics.GenericAPIView):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'uuid'

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

