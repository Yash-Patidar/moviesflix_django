from django.db import models

# Create your models here.


class Info(models.Model):
    CHOICES = (
        ('YouTube', 'YouTube'),
        ('Hotstar', 'Hotstar'),
        ('NF', 'Netflix'),
        ('PV', 'Prime Videos'),
        ('HU', 'hulu'),
    )
    Stream = models.CharField(max_length=30, choices=CHOICES, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    imdb = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    play = models.CharField(max_length=2000)
    poster = models.URLField(null=True)
    icon = models.URLField(max_length=500, null=True)
    more = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
