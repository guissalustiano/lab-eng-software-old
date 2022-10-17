from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm, RouteSearchForm

# Create your views here.
def first_view(request):
	return render(request, "FIRST.html")

def login_view(request):
	return render(request, "login.html")

def index_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			login = form.cleaned_data['login']
			password = form.cleaned_data['password']
			print(login, password)

			authenticated = True
			if login == 'admin@mail.com':
				policy = {'route': True, 'flight': True, 'report': True}
			elif login == 'operator@mail.com':
				policy = {'route': True, 'flight': False, 'report': False}
			elif login == 'pilot@mail.com':
				policy = {'route': False, 'flight': True, 'report': False}
			elif login == 'manager@mail.com':
				policy = {'route': False, 'flight': False, 'report': True}
			else:
				authenticated = False
				
			if authenticated:
				return render(
					request, 
					"index.html", 
					{'form': form, 'policy': policy, 'name': login}
				)
	return HttpResponseRedirect('/login')


def route_update_view(request):
	return render(request, "route/update.html")

def route_code_view(request, code: str):
	context = {'code': code}
	return render(request, "route/[code].html", context)

def route_search_view(request):
	if request.method == 'POST':
		form = RouteSearchForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			return HttpResponseRedirect(f'/route/{name}')

	return render(request, "route/search.html")

def report_filter_view(request):
	return render(request, "report/filter.html")

def report_result_view(request):
	return render(request, "report/result.html")

def flight_create_view(request):
	return render(request, "flight/create.html")

def flight_index_view(request):
	return render(request, "flight/index.html")

def flight_update_view(request):
	return render(request, "flight/update.html")

def flight_code_view(request, code: str):
	context = {'code': code}
	return render(request, "flight/[code].html", context)