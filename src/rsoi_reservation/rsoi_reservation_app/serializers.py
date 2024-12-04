from rest_framework import serializers

from rsoi_reservation_app.models import Reservation


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'reservation_uid', 'username', 'book_uid', 'library_uid', 'status', 'start_date', 'till_date']