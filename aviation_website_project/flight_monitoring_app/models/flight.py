from django.db import models
from .route import Route

class Flight(models.Model):
	code = models.CharField(max_length=32, unique=True, null=False)
	status = models.CharField(max_length=32, null=False)
	departure = models.DateTimeField(null=False)
	arrival = models.DateTimeField(null=False)
	route = models.ForeignKey(Route, on_delete=models.CASCADE)

	class Meta:
		db_table = 'company'