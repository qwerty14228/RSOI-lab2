from django.http import HttpResponse

from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import action

from rsoi_gateway.settings import SERVICE_URLS
from rsoi_gateway_app.clients import LibraryClient, RatingClient, ReservationClient

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


class RatingViewSet(viewsets.ViewSet):
   client = RatingClient(SERVICE_URLS['rating'])

   def list(self, request):
      if not request.user.is_authenticated:
         return Response(status=401)
      rating = self.client.get_rating(user=request.user)
      if rating is None:
         return Response(status=404)
      return Response(rating)


class ReservationViewSet(viewsets.ViewSet):
   reservation_client = ReservationClient(SERVICE_URLS['reservation'])
   library_client = LibraryClient(SERVICE_URLS['library'])
   rating_client = RatingClient(SERVICE_URLS['rating'])

   def list(self, request):
      if not request.user.is_authenticated:
         return Response(status=401)
      reservations = self.reservation_client.get_reservations(user=request.user)
      for _ in reservations:
         #TODO: book, library в ответе
         pass
      return Response(reservations)

   def create(self, request):
      if not request.user.is_authenticated:
         return Response(status=401)
      reservations = self.reservation_client.get_reservations(user=request.user, status='RENTED')
      rating = self.rating_client.get_rating(user=request.user)
      if rating is None or rating['stars'] < len(reservations) + 1:
         return Response(status=403)
      
      body = request.data
      lb = self.library_client.get_library_book(library_uid=body['libraryUid'], book_uid=body['bookUid'])
      if lb is None:
         return Response(status=404)
      available_count = lb['available_count']
      if available_count == 0:
         return Response(status=403)
      reservation = self.reservation_client.create_reservation(
         user=request.user, 
         book_uid=body['bookUid'], 
         library_uid=body['libraryUid'], 
         till_date=body['tillDate']
      )
      self.library_client.update_book_available_count(library_book_id=lb['id'],
                                                      available_count=available_count - 1, user=request.user)
      
      result = reservation
      result['reservationUid'] = result['reservation_uid']
      result['startDate'] = result['start_date']
      result['tillDate'] = result['till_date']
      result["rating"] = rating 
      result["book"] = lb["book"]
      result["library"] = lb["library"]
      result["book"]["bookUid"] = result["book"]["book_uid"]
      result["library"]["libraryUid"] = result["library"]["library_uid"]
      return Response(result)


def healthcheck_view(request):
    
    return HttpResponse("")
