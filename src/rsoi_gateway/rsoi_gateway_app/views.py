from django.http import HttpResponse

from rest_framework import permissions, viewsets

from rest_framework.response import Response
from rest_framework.decorators import action

from rsoi_gateway.settings import SERVICE_URLS
from rsoi_gateway_app.clients import LibraryClient

# from rsoi_gateway_app.serializers import LibrarySerializer


class LibraryViewSet(viewsets.ViewSet):
   client = LibraryClient(SERVICE_URLS['library'])

   def list(self, request):
      qp = request.query_params
      return Response(self.client.get_libraries(page=int(qp.get('page', 1)), size=int(qp.get('size', 10)), city=qp.get('city', '')))
   
   @action(detail=True, methods=['get'], url_name='books', url_path='books')
   def list_books(self, request, pk=None):
      qp = request.query_params
      return Response(self.client.get_library_books(
         library_uid=pk, page=int(qp.get('page', 1)), 
         size=int(qp.get('size', 10)),
         show_all=qp.get('showAll', 'false') == 'true'
      ))


def healthcheck_view(request):
    
    return HttpResponse("")
