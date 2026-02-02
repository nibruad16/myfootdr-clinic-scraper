import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self,base_url,start_url):
        self.base_url = base_url
        self.start_url = start_url

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }


def get_clinic_links(self):

    try:
        response = requests.get(self.start_url,headers=self.headers , timeout=15)

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

    except Exception as e:
        print(f"Error fetching clinic links: {e}")
        return []




    

        
