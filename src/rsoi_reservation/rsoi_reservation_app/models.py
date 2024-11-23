from django.db import models

# Create your models here.
class Resarvation(models.Model):
    reservation_uid = models.UUIDField(verbose_name='Reservation')
    username = models.CharField(max_length=80)
    book_uid = models.UUIDField(verbose_name='Book')
    library_uid = models.UUIDField(verbose_name='Library')
    status = models.CharField(max_length=20)
    start_date = models.DateField()
    till_date = models.DateField()