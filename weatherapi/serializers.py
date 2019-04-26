from rest_framework import serializers
from weatherapi.models import WeatherAPI

class Weather_Details_Serializer(serializers.ModelSerializer):
	class Meta:
		model = WeatherAPI
		fields = ['DATE', 'TMAX', 'TMIN']

class Date_Details_Serializer(serializers.ModelSerializer):
	class Meta:
		model = WeatherAPI
		fields = ['DATE']