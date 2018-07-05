import copy

from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from applications.ads.filters import AdFilter
from applications.ads.models import Ad, AdImageModel
from applications.ads.serializers import AdSerializer, AdListSerializer, AdDetailSerializer
from applications.ads.services import get_ads_in_category
from applications.categories.models import Category
from applications.categories.services import get_bread_crumbs, get_category


class AdListView(ListAPIView):

    serializer_class = AdListSerializer
    queryset = Ad.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend, SearchFilter)
    filter_class = AdFilter
    ordering_fields = ('price', 'created')
    search_fields = ('subject',)

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        category = request.query_params.get('category')
        response.data['max_price'] = self._get_max_price_in_category(category)
        response.data['bread_crumbs'] = get_bread_crumbs(category)
        return response

    def _get_max_price_in_category(self, category):
        if not category:
            return self.queryset.order_by('-price').first().price

        ads = get_ads_in_category(category).order_by('-price')
        if ads:
            return ads.first().price


class AdCreateView(CreateAPIView):

    serializer_class = AdSerializer

    def create(self, request, *args, **kwargs):
        category = get_category(slug=self.request.data.get('category'))
        if not category:
            return Response(
                {'category': _('Category does not exist')}, status=status.HTTP_400_BAD_REQUEST
            )
        data = copy.deepcopy(request.data)
        data.update({'category': category.pk, 'user': self.request.user.pk})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.create_images(
            [v for k, v in self.request.data.items() if k.startswith('files')], serializer.data['pk']
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @classmethod
    def create_images(cls, images, ad_pk):
        ad = Ad.objects.get(pk=ad_pk)
        images = [AdImageModel(image=image, ad=ad) for image in images]
        AdImageModel.objects.bulk_create(images)


class AdDetailView(RetrieveUpdateAPIView):

    serializer_class = AdDetailSerializer
    permission_classes = (AllowAny,)
    queryset = Ad.objects.all()
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.instance.images.all().delete()
        for key, value in self.request.data.items():
            if 'files' in key:
                AdImageModel.objects.create(ad=serializer.instance, image=value)
        serializer.instance.category = Category.objects.get(slug=self.request.data['category'])
        serializer.save()

