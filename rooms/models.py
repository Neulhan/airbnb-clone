# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django_countries.fields import CountryField
from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampModel):
    """  Abstract Item  """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampModel):
    name = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bathrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True, blank=True
    )
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name
