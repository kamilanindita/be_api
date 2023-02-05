from .amazon_body_parser import AmazonBodyParser
from .ebay_body_parser import EbayBodyParser

class Parser:
    def __init__(self, soup, marketplace):
        self.soup = soup
        self.marketplace = marketplace

    def extract(self):
        if(self.marketplace=="amazon"):
            print("amazon extracting")
            amazonBodyParser = AmazonBodyParser(self.soup)
            return amazonBodyParser.get_amazon_extract()

        elif(self.marketplace=="ebay"):
            print("ebay extracting")
            ebayBodyParser = EbayBodyParser(self.soup)
            return ebayBodyParser.get_ebay_extract()
        
    


