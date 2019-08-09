from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class DDPUser(AbstractUser):
	pass # additional fields

	class Meta:
		db_table = 'ddpuser'
		verbose_name_plural = 'DDPUsers'

	def __str__(self):
		return self.username
