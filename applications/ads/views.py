from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from applications.ads.models import Category
from applications.ads.serializers import CategorySerializer


class CategoriesView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        return Response([category[0] for category in qs.values_list('name')])
