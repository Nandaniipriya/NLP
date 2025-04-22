import os
import time
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
from playwright.sync_api import sync_playwright

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["Jobs"]  # Database Name
collection = db["findajob"]  # Collection Name

# Base URL for job listings
BASE_URL = "https://findajob.dwp.gov.uk/search"

# Function to scrape job listings
def scrape_job_listings(base_url=BASE_URL, num_pages=1):
    job_data = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Run browser in headless mode
        page = browser.new_page()

        for current_page in range(1, num_pages + 1):
            page_url = f"{base_url}?page={current_page}"
            print(f"🔍 Scraping page {current_page}: {page_url}")  # Debugging URL

            page.goto(page_url, timeout=60000)

            # Wait for the job listings to load
            page.wait_for_selector('div.search-result', timeout=10000)
            job_listings = page.query_selector_all('div.search-result')

            for job in job_listings:
                try:
                    title = job.query_selector('h3 a').inner_text()
                    job_url = "https://findajob.dwp.gov.uk" + job.query_selector('h3 a').get_attribute('href')
                    company = job.query_selector('ul li strong').inner_text()
                    location = job.query_selector('ul li span').inner_text()

                    # Extract salary safely
                    salary = "Not Available"
                    strong_tags = job.query_selector_all('ul li strong')
                    if len(strong_tags) > 1:
                        salary = strong_tags[1].inner_text()

                    description = job.query_selector('p.search-result-description').inner_text()

                    job_entry = {
                        "Job Title": title,
                        "Job URL": job_url,
                        "Company": company,
                        "Location": location,
                        "Salary": salary,
                        "Description": description,
                        "Scraped At": time.strftime("%Y-%m-%d %H:%M:%S")
                    }

                    job_data.append(job_entry)

                except Exception as e:
                    print(f"⚠️ Error scraping job listing: {e}")

        browser.close()

    return job_data

# Function to insert scraped data into MongoDB
def insert_into_mongodb(data):
    if data:
        collection.insert_many(data)
        print(f"✅ Successfully inserted {len(data)} job listings into MongoDB Atlas!")
    else:
        print("⚠️ No data to insert.")

# Get user input for number of pages
num_pages_to_scrape = int(input("Enter the number of pages you want to scrape: "))

# Scrape and insert into MongoDB
scraped_jobs = scrape_job_listings(num_pages=num_pages_to_scrape)
insert_into_mongodb(scraped_jobs)
