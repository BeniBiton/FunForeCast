import requests
from consts import MESSAGE_TO_GPT, GPT_API_KEY, GPT_ENDPOINT

def get_recommended_temperature(attraction_chosen):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GPT_API_KEY}",
    }

    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": MESSAGE_TO_GPT.format(attraction=attraction_chosen)}],
        "temperature": 0.7
    }

    response_gpt = requests.post(url=GPT_ENDPOINT, headers=headers, json=body)
    response_gpt.raise_for_status()
    data = response_gpt.json()
    response_massage_from_gpt = data["choices"][0]["message"]["content"]

    return response_massage_from_gpt
