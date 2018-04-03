#!/usr/bin/env python 

# Jeeho Song 
# js4892
# get request 

# Require the httparty gem (in Ruby)
# Set up the url and send a GET request to it. The base url is:
# "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"
# => "https://api.nasa.gov/planetary/apod?api_key=RVhEoSzXOlHF1ppmniBuNqFaBp9qI6D7sGlQZINQ"
# Make the request and print out the "url" key in the response, which is the image url


import requests 
import json 

url = 'https://api.nasa.gov/planetary/apod?api_key=RVhEoSzXOlHF1ppmniBuNqFaBp9qI6D7sGlQZINQ'

param = {"date": "2017-10-02"}
r = requests.get(url=url, params=param)
data = r.json()
image_url = data['url']

print (image_url)


