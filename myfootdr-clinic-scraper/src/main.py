from .crawler import Crawler
from .parser import Parser

def main():
    print("Starting MyFootDr Clinic Scraper...")
    
    crawler = Crawler()
    parser = Parser()
    
    # Example usage
    links = crawler.discover_links("http://example.com")
    data = parser.parse_html("<html></html>")
    
    print("Scraping completed.")

if __name__ == "__main__":
    main()
