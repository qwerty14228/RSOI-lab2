from django.db import models

class Library(models.Model):
    library_uid = models.UUIDField(verbose_name='Library', unique=True)
    name = models.CharField(max_length=80)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Books(models.Model):
    books_uid = models.UUIDField(verbose_name='Books', unique=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    CONDITIONS = [
        ('EXELLENT', 'EXELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
    ]
    conditions = models.CharField(max_length=20, choices=CONDITIONS, default='EXELLENT')
    
class LibraryBooks(models.Model):       
    available_count = models.IntegerField(verbose_name='Availability')