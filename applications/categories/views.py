from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from applications.categories.filters import CategoryFilter
from .models import Category
from .serializers import CategorySerializer


class CategoriesListView(ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CategoryFilter

    def get_queryset(self):
        category = self.request.query_params.get('category')
        qs = Category.objects.all()
        return qs if category else qs.filter(parent=None)
