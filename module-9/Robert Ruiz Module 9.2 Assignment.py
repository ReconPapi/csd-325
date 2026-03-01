#This program displays number of astronauts currently in space
import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Print astronaut info
response = requests.get("http://api.open-notify.org/astros.json")
jprint(response.json())