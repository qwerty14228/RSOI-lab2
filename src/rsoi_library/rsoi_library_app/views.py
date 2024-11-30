from rest_framework import permissions, viewsets

from rsoi_library_app.models import Library
from rsoi_library_app.serializers import LibrarySerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('library_uid')
    serializer_class = LibrarySerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
