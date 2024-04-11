from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from io import StringIO
import os


url = "https://us-counties.p.rapidapi.com/summary"

headers = {
	"X-RapidAPI-Key": "5bbb8ab0e6msh6363246616a23adp18e7c6jsn7628ddae2dfb",
	"X-RapidAPI-Host": "us-counties.p.rapidapi.com"
}

# config_file_path = 'config.json'

# with open (config_file_path, 'r') as config_file:
#     config = json.load(config_file)

# X-RapidAPI-Key = config["connectionString"]


# output= StringIO()

# tried = output.getvalue()

# output.close()


response = requests.get(url, headers=headers)
data =response.json()

county_names = [county['name'] for county in data if 'name' in county]
counties_by_state = {}

# Iterate over data
for item in data:
    state = item.get('state')
    county_name = item.get('name')
    if state and county_name:
        # Check if the state already exists in the dictionary
        if state not in counties_by_state:
            counties_by_state[state] = []
        # Append the county name to the list of counties for the state
        counties_by_state[state].append(county_name)

print(counties_by_state)
