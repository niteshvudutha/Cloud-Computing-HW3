from django.urls import path, include
from . import views
from weatherapi.views import DateViewSet, ForecastViewSet, DateListViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

listOfDates = DateListViewSet.as_view({'get':'list', 'post':'create'})

dateInfos = DateViewSet.as_view(
	{
		'get':'retrieve',
		'put' : 'update',
		'patch' : 'partial_update',
		'delete' : 'destroy'
	})

weatherInfos = ForecastViewSet.as_view({'get':'retrieve'})


urlpatterns = [
	path('historical/', listOfDates, name='date-list'),
	path('historical/<int:pk>/', dateInfos, name='date-detail'),
	path('forecast/<int:pk>/', weatherInfos, name='weather-detail'),
	]
