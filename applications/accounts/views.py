from rest_framework import generics
from rest_framework import mixins

from applications.accounts.models import UserProfile
from applications.accounts.serializers import UserProfileSerializer


class UserProfileView(mixins.UpdateModelMixin, generics.GenericAPIView):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

