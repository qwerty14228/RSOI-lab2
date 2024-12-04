from django.http import HttpResponse

from rest_framework import permissions, viewsets

from rsoi_reservation_app.models import Reservation
from rsoi_reservation_app.serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('reservation_uid')
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]


def healthcheck_view(request):
    
    return HttpResponse("")
