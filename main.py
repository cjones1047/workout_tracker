import os
import dotenv

dotenv.load_dotenv()

nutritionix_app_id = os.getenv("APP_ID")
nutritionix_api_key = os.getenv("API_KEY")
