from rest_framework import status
from rest_framework.generics import UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.views import VerifyJSONWebToken
from django.utils.translation import ugettext_lazy as _

from applications.accounts.models import UserProfile
from applications.accounts.serializers import UserProfileSerializer, UserProfileUpdateSerializer, \
    ChangePasswordSerializer


class UserProfileView(UpdateAPIView):

    serializer_class = UserProfileUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = UserProfile.objects.all()
    lookup_field = 'uuid'

    def initial(self, request, *args, **kwargs):
        self.kwargs['uuid'] = request.user.uuid
        super().initial(request, *args, **kwargs)


class UserProfileDestroyView(DestroyAPIView):

    serializer_class = UserProfileUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = UserProfile.objects.all()

    def delete(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.pk
        return self.destroy(request, *args, **kwargs)


class UserVerifyJWT(VerifyJSONWebToken):

    def post(self, request, *args, **kwargs):
        response = super().post(request)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            response.data['user'] = UserProfileSerializer(user).data
        return response


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = UserProfile
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch', 'head', 'options', 'trace']

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': [_('Wrong password.')]}, status=status.HTTP_400_BAD_REQUEST)
            if serializer.data.get('new_password') != serializer.data.get('new_password_confirm'):
                return Response({'new_password_confirm': [_('Confirm password is not the same.')]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
