##Scrapping 
import asyncio
from playwright.async_api import async_playwright
import json

class StartupIndiaScraper:
    def __init__(self, base_url=""):
        self.base_url = base_url
        self.startups = []

    async def scrape_startups(self, max_startups=150000):
        async with async_playwright() as p:
            # Launch browser
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            # Navigate to the page
            await page.goto(self.base_url, wait_until="networkidle")
            
            # Wait for initial content to load
            await page.wait_for_selector('.img-wrap')
            
            async def extract_startup_details():
                # Extract startup details using Playwright's built-in methods
                startup_cards = await page.query_selector_all('.img-wrap')
                
                for card in startup_cards:
                    # Skip if we've reached max startups
                    if len(self.startups) >= max_startups:
                        break
                    
                    try:
                        # Extract name
                        name_elem = await card.query_selector('h3')
                        name = await name_elem.inner_text() if name_elem else 'N/A'
                        
                        # Extract stage
                        stage_elem = await card.query_selector('.highlighted-text')
                        stage = await stage_elem.inner_text() if stage_elem else 'N/A'
                        
                        # Extract location
                        location_elems = await card.query_selector_all('.location span')
                        location = ' '.join([await loc.inner_text() for loc in location_elems]) if location_elems else 'N/A'
                        
                        # Extract department
                        dept_elem = await card.query_selector('.down-dept .dept')
                        department = await dept_elem.inner_text() if dept_elem else 'N/A'
                        
                        # Extract image URL
                        img_elem = await card.query_selector('img')
                        image_url = await img_elem.get_attribute('src') if img_elem else 'N/A'
                        
                        # Create startup info dictionary
                        startup_info = {
                            'name': name.strip(),
                            'stage': stage.strip(),
                            'location': location.strip(),
                            'department': department.strip(),
                            'image_url': image_url
                        }
                        
                        # Avoid duplicates
                        if startup_info not in self.startups:
                            self.startups.append(startup_info)
                        
                    except Exception as e:
                        print(f"Error extracting startup details: {e}")
            
            # Initial extraction
            await extract_startup_details()
            
            # Load more and extract until max startups or no more results
            while len(self.startups) < max_startups:
                try:
                    # Find and click "Load More" button
                    load_more_button = await page.query_selector('#loadmoreicon')
                    
                    if not load_more_button:
                        # No more "Load More" button found
                        break
                    
                    # Click "Load More" button
                    await load_more_button.click()
                    
                    # Wait for new content to load
                    await page.wait_for_timeout(2000)
                    
                    # Extract newly loaded startups
                    await extract_startup_details()
                    
                except Exception as e:
                    print(f"Error during load more: {e}")
                    break
            
            # Close browser
            await browser.close()
            
            return self.startups

    async def save_to_json(self, filename='startups.json'):
        await self.scrape_startups()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.startups, f, ensure_ascii=False, indent=4)
        print(f"Saved {len(self.startups)} startups to {filename}")

async def main():
    scraper = StartupIndiaScraper()
    await scraper.save_to_json()

if __name__ == '__main__':
    asyncio.run(main())
    