from rest_framework.generics import ListAPIView

from applications.ads.models import Category
from applications.ads.serializers import CategorySerializer


class CategoriesView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
