import requests

response = requests.get(
    "http://127.0.0.1:8000/ask",
    params={"q": "When is the closing date for fall 2025"}
)

print(response.json())
