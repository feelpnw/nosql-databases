#!/usr/bin/env python 

# Require the httparty gem

# Set up the url and send a GET request to it. The base url is:
# "https://api.nasa.gov/planetary/apod?api_key=NNKOjkoul8n1CH18TWA9gwngW1s1SmjESPjNoUFo"

# Make the request and print out the "url" key in the response, which is the image url

# "https://api.nasa.gov/planetary/apod?api_key=RVhEoSzXOlHF1ppmniBuNqFaBp9qI6D7sGlQZINQ"

import requests 
import json 

url = 'https://api.nasa.gov/planetary/apod?api_key=RVhEoSzXOlHF1ppmniBuNqFaBp9qI6D7sGlQZINQ'

param = {"date": "2017-10-02"}
r = requests.get(url, params=param)
data = r.json()
image_url = data['url']

print (image_url)





# r = requests.get(url) #(url=url, params=params)
# data = r.json()

# data['date'] = '2017-10-02'
