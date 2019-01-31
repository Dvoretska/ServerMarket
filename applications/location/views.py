import json
from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.views import APIView
import pycountry


class CountryView(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        return Response({country.name: country.alpha_2.lower() for country in pycountry.countries})


# class CitiesView(APIView):
#
#     CACHE_PREFIX = 'country_'
#
#     authentication_classes = ()
#     permission_classes = ()
#
#     def get(self, request, code):
#         cities = cache.get('{}{}'.format(self.CACHE_PREFIX, code.lower()))
#         if not cities:
#             cities = self._get_cities_by_code(code)
#             if cities:
#                 cache.set('{}{}'.format(self.CACHE_PREFIX, code.lower()), cities)
#         return Response(cities)
#
#     @classmethod
#     def _get_cities_by_code(cls, code):
#         with open('applications/location/cities.json') as data_file:
#             data = json.load(data_file)
#         return [city['name'] for city in data if city["country"] == code.upper()]


class CitiesView(APIView):

    CACHE_PREFIX = 'country_'

    authentication_classes = ()
    permission_classes = ()

    def get(self, request, search):
        return Response(self._get_cities_by_code(search.lower()))

    @staticmethod
    def _get_cities_by_code(search):
        result = []
        with open('applications/location/cities_ua.json') as data_file:
            data = json.load(data_file)
        for state in data['areas']:
            for city in state['areas']:
                if city['name'].lower().startswith(search):
                    result.append(f'{city["name"]}, {state["name"]}')
        return result
