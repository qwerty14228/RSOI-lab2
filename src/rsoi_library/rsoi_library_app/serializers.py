from rest_framework import serializers

from rsoi_library_app.models import Library, Books, LibraryBooks


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ['id', 'library_uid', 'name', 'city', 'address']

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'books_uid', 'name', 'author', 'genre', 'condition']

class LibraryBooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LibraryBooks
        fields = ['book_id', 'library_id', 'available_count']