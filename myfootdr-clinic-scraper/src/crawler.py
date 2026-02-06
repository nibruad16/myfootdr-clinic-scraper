import requests
from bs4 import BeautifulSoup
import time


class Crawler:
    def __init__(self,base_url,start_url):
        self.base_url = base_url
        self.start_url = start_url
        
        # Create a session for connection reuse
        self.session = requests.Session()

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }

    def get_clinic_links(self):
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                print(f"🔄 Attempting to fetch clinic links (attempt {attempt + 1}/{max_retries})...")
                
                response = self.session.get(
                    self.start_url,
                    headers=self.headers,
                    timeout=30
                )
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')

                links = []

                for a_tag in soup.find_all('a',href=True):
                    href = a_tag['href']

                    if '/our-clinics/' in href and not href.endswith('/our-clinics/'):
                        full_url = self.base_url + href if href.startswith('/') else href
                        links.append(full_url)

                unique_links = sorted(list(set(links)))

                print(f"✅ Found {len(unique_links)} unique clinic pages.")
                return unique_links

            except requests.exceptions.ConnectionError as e:
                wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                print(f"❌ Connection error: {e}")
                
                if attempt < max_retries - 1:
                    print(f"⏳ Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Failed after {max_retries} attempts.")
                    return []
                    
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                return []




    

        
