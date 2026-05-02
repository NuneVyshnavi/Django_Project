from django.db import models
from donations.models import Donation

# Create your models here.
from django.db import models
from donations.models import Donation


class FoodRequest(models.Model):

    donation = models.ForeignKey(
        Donation,
        on_delete=models.CASCADE
    )

    ngo_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    requested_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.ngo_name