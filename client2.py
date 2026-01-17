import requests
import json
 
def make_request():
    data = {
        "certificate": "dummy_data_for_http",
        "data": "some_data"
    }
 
    url = 'http://localhost:8000/api/data'
 
    print(f"Sending request to {url}")
    print(f"Data: {data}")
 
    try:
        # Уменьшим таймаут для быстрой диагностики
        response = requests.post(url, json=data, timeout=5)
 
        print(f"Status Code: {response.status_code}")
 
        if response.status_code == 200:
            print(f"Success: {response.json()}")
        else:
            print(f"Error: {response.status_code}")
            print(f"Response text: {response.text[:200]}")  # первые 200 символов
 
    except requests.exceptions.Timeout:
        print("Timeout: Request took too long (5 seconds)")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except Exception as e:
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {e}")
 
if __name__ == '__main__':
    make_request()
