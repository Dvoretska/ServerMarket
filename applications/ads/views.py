from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from applications.ads.models import Category, Ad
from applications.ads.serializers import CategorySerializer, AdSerializer, AdListSerializer


class CategoriesListView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        return Response([category[0] for category in qs.values_list('name')])


class AdListView(ListAPIView):

    serializer_class = AdListSerializer
    queryset = Ad.objects.all()
    permission_classes = (AllowAny,)


class AdCreateView(CreateAPIView):

    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        try:
            category = Category.objects.get(name=self.request.data.get('category').title())
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



