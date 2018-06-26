from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, DestroyAPIView, get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.ads.models import Ad
from applications.ads.my.models import SavedAd
from applications.ads.my.serializers import SavedAdSerializer, LightSavedAdSerializer
from applications.ads.serializers import AdListSerializer


class MyAdsListView(ListAPIView):

    serializer_class = AdListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Ad.objects.filter(user=self.request.user)


class MyAdDetailView(DestroyAPIView):

    queryset = Ad.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'slug'


class CreateSavedAdView(CreateAPIView):

    serializer_class = LightSavedAdSerializer

    def create(self, request, *args, **kwargs):

        ad = Ad.objects.filter(slug=kwargs['slug']).first()
        if not ad:
            raise NotFound

        request.data.update({
            'user': request.user.pk,
            'ad': ad.pk
        })
        response = super().create(request, *args, **kwargs)
        serializer = AdListSerializer(instance=ad)
        response.data = serializer.data
        return response


class DeleteSavedAdView(DestroyAPIView):
    serializer_class = SavedAdSerializer
    queryset = SavedAd.objects.all()
    lookup_field = 'slug'

    def get_object(self):
        obj = get_object_or_404(self.queryset, ad__slug=self.kwargs[self.lookup_field], user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj


class SavedAdView(ListAPIView):

    serializer_class = AdListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        saved_pk = SavedAd.objects.filter(user=self.request.user).values_list('ad__pk', flat=True)
        return Ad.objects.prefetch_related('savedad_set').filter(pk__in=saved_pk)


class SavedSlugsView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        saved_pk = SavedAd.objects.filter(user=request.user).values_list('ad__pk', flat=True)
        return Response(
            Ad.objects.prefetch_related('savedad_set').filter(pk__in=saved_pk).values_list('slug', flat=True)
        )