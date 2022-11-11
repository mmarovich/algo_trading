import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {
    # "interval":"5min",
    "function":"TIME_SERIES_DAILY",
    "symbol":"GOOG",
    "datatype":"json",
    "output_size":"full"
}

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


