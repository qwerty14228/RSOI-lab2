from rest_framework import serializers

from rsoi_library_app.models import Library


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'library_uid', 'name', 'city', 'address']