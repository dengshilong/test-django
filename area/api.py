from rest_framework import generics
from .cache import city_cache
from .serializer import AreaSerializer
class CityListAPI(generics.ListAPIView):
    serializer_class = AreaSerializer

    def get_queryset(self):
        return city_cache(self._province)

    def get(self, request, *args, **kwargs):
        self._province = kwargs['province']
        return super(CityListAPI, self).get(request, *args, **kwargs)
