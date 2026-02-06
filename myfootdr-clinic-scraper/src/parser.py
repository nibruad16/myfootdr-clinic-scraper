import requests
from bs4 import BeautifulSoup
import time


class Parser:
    @staticmethod
    def scrape_details(url):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                res = requests.get(url, headers=headers, timeout=15)
                res.raise_for_status()
                soup = BeautifulSoup(res.text,'html.parser')


                name = soup.find('h1').get_text(strip=True) if soup.find('h1') else "N/A"

                address = soup.find('address')

                address = address.get_text(separator=" ", strip=True) if address else "N/A"

                phone = "N/A"

                tel_link = soup.find('a', href=lambda x: x and x.startswith('tel:'))

                if tel_link:
                    phone = tel_link.get_text(strip=True)

                email = "N/A"

                mail_link = soup.find('a', href=lambda x: x and x.startswith('mailto:'))

                if mail_link:
                    email = mail_link.get_text(strip=True)
                

                services_list = []

                for li in soup.find_all('li'):
                    if 'services' in str(li.parent.get('class', [])).lower() or 'service' in str(li.parent.get('id', '')).lower():
                        services_list.append(li.get_text(strip=True))

                services = ", ".join(services_list) if services_list else "General Podiatry"


                return {
                    "Name of Clinic": name,
                    "Address": address,
                    "Email": email,
                    "Phone": phone,
                    "Services": services
                }

            except requests.exceptions.ConnectionError as e:
                wait_time = 2 ** attempt
                if attempt < max_retries - 1:
                    print(f"⏳ Connection error, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print(f"❌ Error fetching clinic details after {max_retries} attempts: {e}")
                    return None
                    
            except Exception as e:
                print(f"❌ Error fetching clinic details: {e}")
                return None
            


        



            