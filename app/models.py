from django.db import models

# Create your models here.
class Plan_info(models.Model):
    DESTINATION_CHOICES = [
        ('europe', 'Europe'),
        ('asia', 'Asia'),
        ('america', 'America'),
        ('africa','Africa'),
        ('australia', 'Australia'),

    ]
    TOUR_CHOICES = [
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('relaxation', 'Relaxation'),
        ('family', 'Family'),
        ('luxury', 'Luxury'),
    ]
    destination = models.CharField(max_length=10, choices=DESTINATION_CHOICES)
    departure_date = models.DateField()
    return_date = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    tour_type = models.CharField(max_length=10, choices=TOUR_CHOICES)
    image = models.ImageField(upload_to='destinations/', blank=True)

    def __str__(self):
        return self.destination
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)