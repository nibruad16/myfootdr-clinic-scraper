import time
import pandas as pd
from crawler import Crawler
from parser import Parser


BASE_URL = "https://web.archive.org"
START_URL = "https://web.archive.org/web/20250708180027/https://www.myfootdr.com.au/our-clinics/"

def run_scraper():
    crawler = Crawler(BASE_URL,START_URL)
    links = crawler.get_clinic_links()


    all_data = []

    for i, link in enumerate(links):
        print(f"[{i+1}/{len(links)}] Scraping: {link}")

        data = Parser.scrape_details(link)

        # Only append if data was successfully scraped
        if data is not None:
            all_data.append(data)
    
        time.sleep(1.5)

        # Filter out any None values and save progress
        valid_data = [d for d in all_data if d is not None]
        
        if valid_data:  # Only create CSV if we have valid data
            df = pd.DataFrame(valid_data)
            df.to_csv('data/clinics_data.csv', index=False)

if __name__ == "__main__":
    run_scraper()


   

   




