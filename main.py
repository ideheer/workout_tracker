import requests
from datetime import datetime

N_APP_ID = "379b4604"
N_API_KEY = "2cb0059df596ab7cbd34e2543626abc2"
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

# response = requests.post(url=exercise_endpoint, json=data_entry, headers=headers)
# result = response.json()
# print(result)

# today = datetime.now()
# date = today.strftime("%d"+"/"+"%m"+"/"+"%Y")
# time = today.strftime("%H:%M:%S")
# exercise = result["exercises"][0]["name"]
# duration = result["exercises"][0]["duration_min"]
# calories = result["exercises"][0]["nf_calories"]

sheety_endpoint = "https://api.sheety.co/9812358a3e25c44b28f5bca7cf88eec1/workouts/workouts?valueInputOption=user_entered'"
params = {
    "workout": {
        "date": "18/08/2023",
        "time": "19:00",
        "exercise": "running",
        "duration": "22",
        "calories": "120",
    },
}

sheety_response = requests.post(url=sheety_endpoint, json=params, headers={"Content-Type": "application/json"})
print(sheety_response.text)
