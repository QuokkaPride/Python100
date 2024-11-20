import requests

def get_questions():
    response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
    response.raise_for_status()
    return response.json()["results"]

question_data = get_questions()
