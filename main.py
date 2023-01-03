import os
import dotenv
import requests

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
print(exercise_response.text)
