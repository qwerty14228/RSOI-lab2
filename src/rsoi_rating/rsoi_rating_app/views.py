from rest_framework import permissions, viewsets

from rsoi_rating_app.models import Rating
from rsoi_rating_app.serializers import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('username')
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]