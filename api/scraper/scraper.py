from .body_parser import Parser
from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        # Extract marketplace from url
        marketplace = self.url.split(".")[1]

        if(marketplace=="amazon" or marketplace=="ebay"):
            headers = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})

            # proxy = 'http://14.198.21.70:80'

            # HTTP Request
            webpage = requests.get(self.url, headers=headers, timeout=30)

            if(webpage.status_code == 200):
                # Soup Object containing all data
                soup = BeautifulSoup(webpage.content, "lxml")

                # Parser
                parse = Parser(soup, marketplace)
                return parse.extract()
                
            elif(webpage.status_code == 503):
                print("rate limit")
                return "rate limit"
            
        else:
            return "marketplace not available"
