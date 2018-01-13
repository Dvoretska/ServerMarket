from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.views import VerifyJSONWebToken

from applications.accounts.models import UserProfile
from applications.accounts.serializers import UserProfileSerializer, UserProfileUpdateSerializer


class UserProfileView(generics.UpdateAPIView):

    serializer_class = UserProfileUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = UserProfile.objects.all()
    lookup_field = 'uuid'

    def initial(self, request, *args, **kwargs):
        self.kwargs['uuid'] = request.user.uuid
        super(UserProfileView, self).initial(request, args, kwargs)


class UserVerifyJWT(VerifyJSONWebToken):

    def post(self, request, *args, **kwargs):
        response = super(UserVerifyJWT, self).post(request)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            response.data['user'] = UserProfileSerializer(user).data
        return response
