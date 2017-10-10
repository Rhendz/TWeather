# Responsible for receiving and updating the cities in Tennessee.

# Scrapes wikipedia for latitude and longitude data
# for municipalities within TN and outputs all of
# the data in a JSON file.

# Example: wikipedia.page(title="Adams, Tennessee", pageid=None, auto_suggest=True, redirect=True, preload=False).coordinates

import wikipedia

# Gets Place Name from https://en.wikipedia.org/wiki/List_of_municipalities_in_Tennessee
cities = wikipedia.page(title="List_of_municipalities_in_Tennessee", pageid=None, auto_suggest=True, redirect=True, preload=False).links