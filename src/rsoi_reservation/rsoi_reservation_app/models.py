from django.db import models

class Resarvation(models.Model):
    reservation_uid = models.UUIDField(verbose_name='Reservation', unique=True)
    username = models.CharField(max_length=80)
    book_uid = models.UUIDField(verbose_name='Book')
    library_uid = models.UUIDField(verbose_name='Library')

    STATUSES = [
        ('RENTED', 'RENTED'),
        ('RETURNED', 'RETURNED'),
        ('EXPIRED', 'EXPIRED'),
    ]
    status = models.CharField(max_length=20, choices=STATUSES)
    start_date = models.DateTimeField()
    till_date = models.DateTimeField()