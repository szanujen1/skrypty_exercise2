import requests
import json


def get_intent(sentence):
    url = "http://localhost:5005/model/parse"
    payload = {'text': sentence}
    response = requests.post(url, json=payload)
    return response.json()


response = get_intent("add candidate")
print(json.dumps(response, indent=2))
