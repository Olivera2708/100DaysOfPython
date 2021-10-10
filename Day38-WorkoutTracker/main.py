import requests
from datetime import datetime

API_KEY = ""
API_ID = ""

GENDER = ""
WEIGHT = 
HEIGHT = 
AGE = 

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
api_sheety = "https://api.sheety.co/61fe0298575e162c657cddd733dd40ba/workout/лист1"

hearder = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

sentence = input("Tell me what you did today -> ")

params = {
    "query": sentence,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=endpoint, json=params, headers=hearder)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "лист1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

bearer_headers = {
    "Authorization": "Bearer 123123123"
}
sheet_response = requests.post(
    api_sheety, 
    json=sentence, 
    headers=bearer_headers
)

response = requests.post(api_sheety, json=sheet_input)
print(response.text)
