import requests
import random
from logger import log_retry

API_URL = "https://jsonplaceholder.typicode.com/posts"
API_KEY = "my-secret-api-key"  # simulate secure key

def send_to_api(data: dict) -> bool:
    try:
        # Simulate random API failure
        if random.random() < 0.2:
            print("Simulated API failure")
            return False

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(API_URL, json=data, headers=headers, timeout=5)

        return response.status_code == 201

    except Exception as e:
        print(f"API Error: {e}")
        return False
    
def send_with_retry(data: dict, retries: int = 3) -> bool:
    email = data.get("email_address")
    for attempt in range(1, retries + 1):
        success = send_to_api(data)
        if success:
            return True
        log_retry(email, attempt)

    return False