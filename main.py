import os
import dotenv
import requests
import datetime

dotenv.load_dotenv()

nutritionix_app_id = os.getenv("APP_ID")
nutritionix_api_key = os.getenv("API_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key,
    "Content-Type": "application/json"
}

json = {
    "query": input("Tell me which exercise you did:\n")
}

exercise_response = requests.post(url=exercise_endpoint, headers=headers, json=json)
exercise_response.raise_for_status()
exercise_response = exercise_response.json()

sheety_endpoint = "https://api.sheety.co/5c0890de0bca32e2dc600cbaa0236156/myWorkouts/workouts"
current_date = datetime.date.today().strftime('%d/%m/%Y')
current_time = datetime.datetime.now().strftime('%H:%M:%S')
sheety_token = os.getenv("SHEETY_TOKEN")
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

for exercise in exercise_response["exercises"]:
    sheety_post = {
        "workout": {
            "date": f"{current_date}",
            "time": f"{current_time}",
            "exercise": f"{exercise['name'].title()}",
            "duration": f'{exercise["duration_min"]}',
            "calories": f'{exercise["nf_calories"]}'
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_post)
    sheety_response.raise_for_status()
