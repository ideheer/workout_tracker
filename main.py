import requests
from datetime import datetime
import os

N_APP_ID = os.environ["N_APP_ID"]
N_API_KEY = os.environ["N_API_KEY"]
BEARER = os.environ["BEARER_TOKEN"]
GENDER = "male"
WEIGHT = 80
HEIGHT = 182.88
AGE = 42


headers = {
    "x-app-id": N_APP_ID,
    "x-app-key": N_API_KEY,
    "x-remote-user-id": "0",
}

data_entry = {
    "query": input("What exercise did you do today? "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": 42
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=data_entry, headers=headers)
result = response.json()
print(result)

today = datetime.now()
date = today.strftime("%d"+"/"+"%m"+"/"+"%Y")
time = today.strftime("%H:%M:%S")

headers = {
    "Authorization": BEARER
}
sheety_endpoint = "https://api.sheety.co/9812358a3e25c44b28f5bca7cf88eec1/workouts/workouts"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers)
    print(sheety_response.text)
