from django.db import models

# Create your models here.

class Donation(models.Model):
    food_name = models.CharField(max_length=100)
    category = models.CharField(
    max_length=100,
    default='General'
    )
    quantity = models.IntegerField()
    description = models.TextField()
    expiry_time = models.DateTimeField()
    image = models.ImageField(
        upload_to = 'food_images/',
        blank = True,
        null = True
    )

    def __str__(self):
        return self.food_name
