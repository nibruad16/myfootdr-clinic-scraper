from .crawler import Crawler
from .parser import Parser

def main():
    print("Starting MyFootDr Clinic Scraper...")
    
    crawler = Crawler()
    parser = Parser()
    
    # Example usage
    links = crawler.discover_links()
    
    print(f"Discovered {len(links)} links. Printing first 5:")
    for link in links[:5]:
        print(link)
    
    # Placeholder for parsing
    # for link in links:
    #     html = crawler.fetch_page(link)
    #     data = parser.parse_html(html)

if __name__ == "__main__":
    main()
