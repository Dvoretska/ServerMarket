from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from applications.ads.models import Ad
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
