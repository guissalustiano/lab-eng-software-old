"""aviation_website_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from flight_monitoring_app import views

# from django.shortcuts import render

# # Create your views here.
# def first_view(request):
# 	return render(request, "FIRST.html")

# def login_view(request):
# 	return render(request, "login.html")

# def index_view(request):
# 	return render(request, "index.html")

# def route_update_view(request):
# 	return render(request, "route/update.html")

# def route_abxy_view(request):
# 	return render(request, "route/[code].html")

# def route_search_view(request):
# 	return render(request, "route/search.html")

# def report_filter_view(request):
# 	return render(request, "report/filter.html")

# def report_result_view(request):
# 	return render(request, "report/result.html")

# def flight_create_view(request):
# 	return render(request, "flight/create.html")

# def flight_index_view(request):
# 	return render(request, "flight/index.html")

# def flight_update_view(request):
# 	return render(request, "flight/update.html")

# def flight_abxy_view(request):
# 	return render(request, "flight/[code].html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FIRST', views.first_view),
    path("login", views.login_view),
    path("", views.index_view),
    path("route/update", views.route_update_view),
    path("route/<str:code>", views.route_code_view),
    path("route/search", views.route_search_view),
    path("report/filter", views.report_filter_view),
    path("report/result", views.report_result_view),
    path("flight/create", views.flight_create_view),
    path("flight/index", views.flight_index_view),
    path("flight/update", views.flight_update_view),
    path("flight/<str:code>", views.flight_code_view),
]
