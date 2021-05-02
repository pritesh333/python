import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "api key",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
info=response.json()

place=info['state_wise']
state=place['Maharashtra']
dist=state['district']
city=dist['Pune']
active=city['active']
confirmed=city['confirmed']
deceased=city['deceased']
recovered=city['recovered']

print("STATE: MAHARASHTRA")
print("CITY: PUNE")
print("ACTIVE CASES:",active)
print("CONFIRMED CASES:",confirmed)
print("RECOVERED:",recovered)
print("DEATHS:",deceased)


input("Press Enter to continue...")
