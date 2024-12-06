from django.http import HttpResponse

from rest_framework import permissions, viewsets

from rest_framework.response import Response

from rsoi_gateway.settings import SERVICE_URLS
from rsoi_gateway_app.clients import LibraryClient

# from rsoi_gateway_app.serializers import LibrarySerializer


class LibraryViewSet(viewsets.ViewSet):
   client = LibraryClient(SERVICE_URLS['library'])

   def list(self, request):
      return Response(self.client.get_libraries(**request.query_params))


def healthcheck_view(request):
    
    return HttpResponse("")
