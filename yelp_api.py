import forecastio
from geopy.geocoders import Nominatim
import os
from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.client import Client
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
    api_key = os.environ['FORECASTIO_API_KEY']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)

def get_businesses(location, term):
	auth = Oauth1Authenticator(
 		consumer_key=os.environ['CONSUMER_KEY'],
    	consumer_secret=os.environ['CONSUMER_SECRET'],
    	token=os.environ['TOKEN'],
    	token_secret=os.environ['TOKEN_SECRET']
    )

	client = Client(auth)

	params = {
    	'term': term,
    	'lang': 'en',
    	'limit': 3
	}

	response = client.search(location, **params)
	
	businesses = []

	for business in response.businesses:
		businesses.append({"name": business.name, 
			"rating": business.rating, 
			"phone": business.phone,
		})

	return businesses

