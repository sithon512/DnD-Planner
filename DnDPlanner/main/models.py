"""
Defines all of the database models.
"""

from django.conf import settings
from django.db import models

# standard models
class Campaign(models.Model):
	title = models.CharField(max_length=50, verbose_name='Campaign Title')
	description = models.TextField(verbose_name='Description')
	ofk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Location(models.Model):
	name = models.CharField(max_length=50, verbose_name='Location Name')
	description = models.TextField(verbose_name='Description')
	ofk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Encounter(models.Model):
	name = models.CharField(max_length=50, verbose_name='Encounter Name')
	description = models.TextField(verbose_name='Description')
	ofk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Item(models.Model):
	name = models.CharField(max_length=50, verbose_name='Item Name')
	description = models.TextField(verbose_name='Description')
	ofk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Creature(models.Model):
	name = models.CharField(max_length=50, verbose_name='Creature Name')
	description = models.TextField(verbose_name='Description')
	ofk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class PlotMoment(models.Model):
	name = models.CharField(max_length=50, verbose_name='Plot Moment Name')
	description = models.TextField(verbose_name='Description')
	ofk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

# mapping tables