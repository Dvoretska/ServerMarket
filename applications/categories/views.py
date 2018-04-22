from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from applications.categories.filters import CategoryFilter
from .models import Category
from .serializers import CategorySerializer


class CategoriesListView(ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CategoryFilter

    def get_queryset(self):
        category_params = self.request.query_params.get('category')
        category_param = category_params.split(',')[0] if category_params else []
        self.request.query_params._mutable = True
        qs = Category.objects.all()
        category = Category.objects.filter(slug=category_param).first()
        if not category or not category_param:
            self.request.query_params['category'] = None
            return qs.filter(parent=None)
        elif category.is_leaf_node():
            self.request.query_params['category'] = category.parent.slug
        return qs

