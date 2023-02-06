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
            headers = ({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"})
            
            # HTTP Request
            webpage = requests.get(self.url, headers=headers, timeout=None)

            # Soup Object containing all data
            soup = BeautifulSoup(webpage.content, "lxml")

            # Parser
            parse = Parser(soup, marketplace)
            return parse.extract()
            
        else:
            return "marketplace not available"
