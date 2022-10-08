from django.db import models
import datetime

# Create your models here.
class Airport(models.Model):
	name = models.CharField(max_length=256, null=False)
	code = models.CharField(max_length=32, unique=True, null=False)
	city = models.CharField(max_length=256, null=False)

	class Meta:
		db_table = 'airport'

class Company(models.Model):
	name = models.CharField(max_length=256, null=False)
	website = models.CharField(max_length=512, null=False)

class Route(models.Model):

	class DayOfWeek(models.IntegerChoices):
		monday = 0
		tuesday = 1
		wednesday = 2
		thursday = 3
		friday = 4
		saturday = 5
		sunday = 6

	code = models.CharField(max_length=32, unique=True, null=False)
	schedule = models.TimeField(null=False)
	day_of_week = models.IntegerField(choices=DayOfWeek.choices, null=False)
	duration = models.DurationField(null=False)
	departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
	arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	class Meta:
		db_table = 'route'

class Flight(models.Model):
	code = models.CharField(max_length=32, unique=True, null=False)
	status = models.CharField(max_length=32, null=False)
	departure = models.DateTimeField(null=False)
	arrival = models.DateTimeField(null=False)
	route = models.ForeignKey(Route, on_delete=models.CASCADE)

	class Meta:
		db_table = 'company'