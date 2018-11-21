from django.db import models
from django.forms import ModelForm
from django import forms

GENRE_CHOICES = (
    ('ACTION', 'Action'),
    ('COMEDY', 'Comedy'),
    ('ROMANCE', 'Romance'),
    ('HORROR', 'Horror'),
    ('THRILLER', 'Thriller'),
)

class Movie(models.Model):
    ACTION = 'Action'
    COMEDY = 'Comedy'
    ROMANCE = 'Romance'
    HORROR = 'Horror'
    THRILLER = 'Thriller'
    name = models.CharField(max_length=200)
    released = models.DateField('date released')
    duration = models.TimeField()
    price = models.FloatField()
    rentedby = models.ForeignKey('Customer',on_delete=models.SET_NULL,null=True,)

    genre = models.CharField(
        choices = GENRE_CHOICES,
        default = ACTION,
        max_length = 15,
    )
    class Meta:
        db_table = "Movie"

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    age = models.IntegerField()

    class Meta:
        db_table = "Customer"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class MovieForm(forms.Form):
    name = forms.CharField(label='Name', max_length='200')
    released = forms.DateField(label='Date Released')
    duration =  forms.TimeField(label='Duration')
    price = forms.FloatField(label='Price')
    genre = forms.CharField(label='Genre', max_length='15', widget=forms.Select(choices=GENRE_CHOICES))
