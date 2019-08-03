from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class DDPUser(AbstractUser):
	pass # additional fields

	def __str__(self):
		return self.email
