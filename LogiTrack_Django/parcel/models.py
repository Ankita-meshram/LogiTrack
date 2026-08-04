import uuid
from django.db import models


class Parcel(models.Model):
    tracking_id = models.CharField(max_length=20, unique=True, editable=False)

    sender_name = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=15)
    sender_address = models.TextField()

    receiver_name = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=15)
    receiver_address = models.TextField()

    parcel_type = models.CharField(max_length=50)

    weight = models.FloatField()

    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('In Transit', 'In Transit'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Booked'
    )

    booking_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            self.tracking_id = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.tracking_id