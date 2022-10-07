from django.test import TestCase
from flight_monitoring_app.models import (
	Airport, 
	Company, 
	Flight, 
	Route
)

# Create your tests here.
class CompanyModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Company.objects.create(name='Test Company', website='https://www.test.com')

	def test_name_label(self):
		company = Company.objects.get(id=1)
		field_label = company._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')

	def test_website_label(self):
		company = Company.objects.get(id=1)
		field_label = company._meta.get_field('website').verbose_name
		self.assertEquals(field_label, 'website')

	def test_name_max_length(self):
		company = Company.objects.get(id=1)
		max_length = company._meta.get_field('name').max_length
		self.assertEquals(max_length, 256)

	def test_website_max_length(self):
		company = Company.objects.get(id=1)
		max_length = company._meta.get_field('website').max_length
		self.assertEquals(max_length, 512)

	def test_object_name_is_name(self):
		company = Company.objects.get(id=1)
		expected_object_name = f'{company.name}'
		self.assertEquals(expected_object_name, str(company))

	def test_get_absolute_url(self):
		company = Company.objects.get(id=1)
		self.assertEquals(company.get_absolute_url(), '/flight_monitoring_app/company/1')