from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):
    
    class Genre(models.TextChoices):
        ROCK = 'Rock'
        POP = 'Pop'
        METAL = 'Metal'
        PUNK = 'Punk'
        JAZZ = 'Jazz'
        BLUES = 'Blues'
        COUNTRY = 'Country'
        ELECTRONIC = 'Electronic'
        HIPHOP = 'Hip-Hop'
        RAP = 'Rap'
        REGGAE = 'Reggae'
        FOLK = 'Folk'
        CLASSICAL = 'Classical'
        OTHER = 'Other'
    
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=15)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Album(models.Model):
    
    class Format(models.TextChoices):
        CD = 'CD'
        VINYL = 'Vinyl'
        DIGITAL = 'Digital'
        CASSETTE = 'Cassette'
        OTHER = 'Other'
    
    title = models.fields.CharField(max_length=100)
    release_year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    band = models.fields.CharField(max_length=100)
    format = models.fields.CharField(choices=Format.choices, max_length=15)
    description = models.fields.CharField(max_length=1000)
    price = models.fields.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    available = models.fields.BooleanField(default=True)