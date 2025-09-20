import json
import ssl
from urllib.request import urlopen
def main():
    url ="https://api.weather.gov/points/40.1934,-85.3864"
    forcast="https://api.weather.gov/gridpoints/IND/83,90/forecast"
    context = ssl._create_unverified_context()
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    response = urlopen(forcast, context=context)
    weatherData = json.loads(response.read())
    print(len(weatherData["properties"]))
    for event in weatherData["properties"]:
        print(event["name"]["temperature"]["detailedForecast"])
main()