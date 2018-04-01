from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoriesListView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
        return Response([category[0] for category in qs.values_list('name')])
