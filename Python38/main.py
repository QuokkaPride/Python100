import requests
from datetime import datetime

APP_ID = "858a28fd"
API_KEY = "5a51a10ac982449fe8894537ad584954"

# Uncomment the line below to take user input
exercise = input("What exercise did you do and for how long?")
# exercise = "I danced for 14 minutes and then hiked for 5 hours then lifted weights for 1 hour"

# Nutritionix endpoint
nutritionix_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"

# Sheety endpoints
SHEETY_GET_ENDPOINT = "https://api.sheety.co/a342ec99e6d9b58df8930172f4e6fb9a/myWorkouts/workouts"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/a342ec99e6d9b58df8930172f4e6fb9a/myWorkouts/workouts"

# Nutritionix headers
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Nutritionix parameters
params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 178,
    "age": 36,
}

# # Sheety get data
# sheet_data_response = requests.get(SHEETY_GET_ENDPOINT).json()

# # Ensure sheet_data_response is a list
# workouts_list = sheet_data_response.get("workouts", [])

# Nutritionix response
exercise_response = requests.post(nutritionix_endpoint, json=params, headers=headers).json()

# Format the exercise response
for exercise in exercise_response["exercises"]:
    workout = {
        "workout": {
            "date": datetime.now().strftime("%m/%d/%Y"),
            "time": datetime.now().strftime("%H:%M"),
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # print(workout)

    # Send the POST request
    response = requests.post(SHEETY_POST_ENDPOINT, json=workout)
    print(response.text)
    
