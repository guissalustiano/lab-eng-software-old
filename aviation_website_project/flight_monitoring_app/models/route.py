from django.db import models

class DayOfWeek(models.IntegerChoices):
		monday = 0
		tuesday = 1
		wednesday = 2
		thursday = 3
		friday = 4
		saturday = 5
		sunday = 6

class Route(models.Model):
	code = models.CharField(max_length=32, unique=True, null=False)
	schedule = models.TimeField(null=False)
	day_of_week = models.IntegerField(choices=DayOfWeek.choices, null=False)
	duration = models.DurationField(null=False)
	departure_airport = models.CharField(max_length=32, unique=True, null=False)
	arrival_airport = models.CharField(max_length=32, unique=True, null=False)
	company = models.CharField(max_length=32, unique=True, null=False)

	class Meta:
		db_table = 'route'