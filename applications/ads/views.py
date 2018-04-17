from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from applications.ads.filters import AdFilter
from applications.ads.models import Ad
from applications.ads.serializers import AdSerializer, AdListSerializer
from applications.categories.models import Category
from applications.categories.services import get_bread_crumbs


class AdListView(ListAPIView):

    serializer_class = AdListSerializer
    queryset = Ad.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AdFilter

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        response.data['bread_crumbs'] = get_bread_crumbs(self.request.query_params.get('category'))
        return response


class AdCreateView(CreateAPIView):

    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(slug=self.request.data.get('category'))
        except ObjectDoesNotExist:
            return Response(
                {'category': _('Category does not exist')}, status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        data['category'] = category.pk
        data['user'] = self.request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



