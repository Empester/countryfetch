import requests
 
response = requests.get("https://www.apicountries.com/capital/jerusalem")
print(response.json())