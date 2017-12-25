from rest_framework.response import Response
from rest_framework.views import APIView
import pycountry


class CountryView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        return Response([country.name for country in pycountry.countries])