from django.test import TestCase
from datetime import datetime, timedelta

from flight_monitoring_app.models import (
	Airport, 
	Company, 
	Flight, 
	Route
)

class CompanyModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Company.objects.create(name='Azul', website='https://www.test.com')

	def test_generate_id(self):
		company = Company.objects.get(name='Azul')
		self.assertEqual(company.id, 1)

	def test_update(self):
		company = Company.objects.get(name='Azul')
		company.name = 'Vermelho'
		company.save()
		self.assertEquals(company.name, 'Vermelho')

	def test_delete(self):
		company = Company.objects.get(name='Azul')
		company.delete()
		self.assertEqual(Company.objects.count(), 0)

class AirportModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Airport.objects.create(name='Guarulhos', code='GRU', city='São Paulo')

	def test_generate_id(self):
		airport = Airport.objects.get(code='GRU')
		self.assertEqual(airport.id, 1)

	def test_update(self):
		airport = Airport.objects.get(code='GRU')
		airport.name = 'Guarulhoz'
		airport.save()
		self.assertEquals(airport.name, 'Guarulhoz')

	def test_delete(self):
		airport = Airport.objects.get(code='GRU')
		airport.delete()
		self.assertEqual(Airport.objects.count(), 0)

class FlightModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		airport1 = Airport.objects.create(name='Airport 1', code='AP1', city='São Paulo')
		airport2 = Airport.objects.create(name='Airport 2', code='AP2', city='São Paulo')
		company = Company.objects.create(name='Company', website='https://www.test.com')

		route = Route.objects.create(
			code='L512',
			schedule=datetime.time(datetime.now()),
			day_of_week=Route.DayOfWeek.monday,
			duration=timedelta(hours=1),
			departure_airport=airport1,
			arrival_airport=airport2,
			company=company
		)

		Flight.objects.create(
			code='L512-01',
			status='Embarque',
			departure=datetime.now(),
			arrival=datetime.now(),
			route=route,
		)

	def test_generate_id(self):
		airport = Flight.objects.get(code='L512-01')
		self.assertEqual(airport.id, 1)

	def test_update(self):
		airport = Flight.objects.get(code='L512-01')
		airport.status = 'Em Voo'
		airport.save()
		self.assertEquals(airport.status, 'Em Voo')

	def test_delete(self):
		airport = Flight.objects.get(code='L512-01')
		airport.delete()
		self.assertEqual(Flight.objects.count(), 0)

class RouteModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		gru_airport = Airport.objects.create(name='Galileu', code='GLL', city='Rio Janeiro')
		cgn_airport = Airport.objects.create(name='Congonhas', code='CNG', city='São Paulo')
		company = Company.objects.create(name='Azul', website='https://www.test.com')

		Route.objects.create(
			code='L512',
			schedule=datetime.time(datetime.now()),
			day_of_week=Route.DayOfWeek.monday,
			duration=timedelta(hours=1),
			departure_airport=gru_airport,
			arrival_airport=cgn_airport,
			company=company
		)

	def test_generate_id(self):
		route = Route.objects.get(code='L512')
		self.assertEqual(route.id, 1)

	def test_update(self):
		route = Route.objects.get(code='L512')
		route.duration = timedelta(hours=2)
		route.save()
		self.assertEquals(route.duration, timedelta(hours=2))

	def test_delete(self):
		route = Route.objects.get(code='L512')
		route.delete()
		self.assertEqual(Route.objects.count(), 0)