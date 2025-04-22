import os
import requests
import json
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
import time

load_dotenv()
API_KEY = os.getenv('TOMTOM_API_KEY')

if not API_KEY:
    raise ValueError("TOMTOM_API_KEY not found in .env file")

# Updated bounding boxes with better coverage
areas = [
    {"name": "Chandigarh", "bbox": "30.68,76.69,30.78,76.84"},
    {"name": "Mohali", "bbox": "30.66,76.68,30.73,76.75"},
    {"name": "Panchkula", "bbox": "30.68,76.84,30.74,76.93"},
    {"name": "Zirakpur", "bbox": "30.61,76.80,30.67,76.88"}
]

# Updated traffic_scrapper.py with enhanced error handling
# Modified get_traffic_data function
def get_traffic_data(area_name, bbox):
    """Get traffic incidents from TomTom API (version 5)"""
    url = "https://api.tomtom.com/traffic/services/5/incidentDetails"
    
    params = {
        "key": API_KEY,
        "bbox": bbox,
        "zoom": 12,
        "fields": "incidents{type,geometry{coordinates},properties{iconCategory,startTime,endTime,delay,roadNumbers}}",
        "language": "en-GB"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return {
            "area": area_name,
            "data": response.json()
        }
    except Exception as e:
        print(f"Error in {area_name}: {str(e)}")
        return {
            "area": area_name,
            "data": None,
            "error": str(e)
        }

# Modified process_traffic_data function
def process_traffic_data(traffic_data):
    """Process API response"""
    if not traffic_data or not traffic_data.get("data"):
        return []
    
    try:
        return [process_incident(incident, traffic_data["area"]) 
               for incident in traffic_data["data"].get("incidents", [])]
    except Exception as e:
        print(f"Processing error in {traffic_data['area']}: {str(e)}")
        return []

def process_incident(incident, area_name):
    """Process individual incident"""
    try:
        return {
            "area": area_name,
            "type": incident.get("type", "N/A"),
            "severity": incident["properties"]["iconCategory"],
            "start": incident["properties"].get("startTime", "N/A"),
            "end": incident["properties"].get("endTime", "N/A"),
            "delay": incident["properties"].get("delay", 0),
            "road": ", ".join(incident["properties"].get("roadNumbers", [])),
            "coordinates": f"{incident['geometry']['coordinates'][0][1]},{incident['geometry']['coordinates'][0][0]}"
        }
    except KeyError as e:
        print(f"Skipping invalid incident in {area_name}: {str(e)}")
        return None

def main():
    # Create output directory if it doesn't exist
    os.makedirs("traffic_data", exist_ok=True)
    
    # Get the current date for filename
    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    all_incidents = []
    
    # Process each area
    for area in areas:
        print(f"Fetching traffic data for {area['name']}...")
        
        # Get traffic data
        traffic_data = get_traffic_data(area['name'], area['bbox'])
        
        # Process into structured format
        processed_incidents = process_traffic_data(traffic_data)
        
        print(f"Found {len(processed_incidents)} incidents in {area['name']}")
        
        # Add to all incidents
        all_incidents.extend(processed_incidents)
        
        # Don't overload the API
        time.sleep(1)
    
    # Convert to DataFrame for easier analysis
    if all_incidents:
        df = pd.DataFrame(all_incidents)
        
        # Save to CSV
        csv_filename = f"traffic_data/traffic_incidents_{current_date}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Saved {len(all_incidents)} traffic incidents to {csv_filename}")
        
        # Save to JSON
        json_filename = f"traffic_data/traffic_incidents_{current_date}.json"
        with open(json_filename, 'w') as f:
            json.dump(all_incidents, f, indent=2)
        print(f"Saved traffic incidents to {json_filename}")
        
        # Print summary by area
        print("\nTraffic Incident Summary:")
        print(df.groupby('area').size())
    else:
        print("No traffic incidents found in any area.")
    
    print(f"Using API key starting with: {API_KEY[:6]}...")

if __name__ == "__main__":
    main()

