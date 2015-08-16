from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):
	user = models.ForeignKey(User)
	company = models.CharField(max_length=200)
	created_date = models.DateTimeField('date created')
	title = models.CharField(max_length=200, blank=True)
	salary_low = models.IntegerField()
	salary_high = models.IntegerField()
	equity_low = models.DecimalField(decimal_places=5, max_digits=9)
	equity_high = models.DecimalField(decimal_places=5, max_digits=9)
	site_used = models.CharField(max_length=400, blank=True)
	cover_used = models.CharField(max_length=100, blank=True)
	resume_used = models.CharField(max_length=100, blank=True)
	notes = models.CharField(max_length=1000, blank=True)
	updated = models.DateTimeField('updated', blank=True)


class Status(models.Model):
	unique_ID = models.ForeignKey(Application)
	updated = models.DateTimeField('status updated')
	status = models.CharField(max_length=50)