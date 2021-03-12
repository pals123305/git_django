from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
	title = models.CharField(max_length=100)
	complete = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=timezone.now())
	due = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
	def __str__(self):
		return self.title