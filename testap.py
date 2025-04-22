# Temporary test script to verify API key
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('TOMTOM_API_KEY')

def verify_key():
    test_url = "https://api.tomtom.com/traffic/services/5/incidentDetails"
    params = {
        "key": API_KEY,
        "bbox": "30.68,76.69,30.78,76.84",
        "zoom": 12
    }
    
    try:
        response = requests.get(test_url, params=params)
        print(f"HTTP Status: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")

print(verify_key())