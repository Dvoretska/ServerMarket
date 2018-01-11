from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from applications.accounts.models import UserProfile
from applications.accounts.permission import IsOwnerOrReadOnly
from applications.accounts.serializers import UserProfileSerializer


class UserProfileView(mixins.UpdateModelMixin, generics.GenericAPIView):

    serializer_class = UserProfileSerializer
    permission_classes = IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    queryset = UserProfile.objects.all()
    lookup_field = 'uuid'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
