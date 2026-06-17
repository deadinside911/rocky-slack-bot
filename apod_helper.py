import os
import requests

from dotenv import load_dotenv

load_dotenv()

NASA_APOD_URL="https://api.nasa.gov/planetary/apod"

print(os.getenv("NASA_API_KEY"))

response = requests.get(NASA_APOD_URL, params={
        "api_key": os.getenv("NASA_API_KEY", "DEMO_KEY"),
})

if response.status_code == 200:
    response_body = response.json()
    print("Image URL:", response_body["hdurl"])
else:
    print("There's something wrong with NASA's APOD API right now, try again in a bit")
