import requests
from bs4 import BeautifulSoup


class Parser:
    @staticmethod
    def scrape_details(url):

        headers = {'User-Agent': 'Mozilla/5.0'}


        try:
            res = requests.get(url,timeout=10)
            soup = BeautifulSoup(res.text,'html.parser')


            name = soup.find('h1').get_text(strip=True) if soup.find('h1') else "N/A"

            address = soup.find('address')

            address = address_tag.get_text(separator=" ", strip=True) if address_tag else "N/A"

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



        except Exception as e:
            print(f"Error fetching clinic details: {e}")
            return None
            


        



            