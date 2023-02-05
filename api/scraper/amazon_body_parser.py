import re
class AmazonBodyParser:
    def __init__(self, soup):
        self.soup = soup

    def get_amazon_extract(self):
        name = self.get_amazon_product_name()
        product_price = self.get_amazon_product_price()
        image_url = self.get_amazon_product_image()

        return {
            "name": name,
            "price": product_price["price"],
            "currency_code": product_price["currency_code"],
            "image_url": image_url,
            "marketplace": "amazon"
        }

    # Extract product name/title
    def get_amazon_product_name(self):
        name= ""
        try:
            name = self.soup.find("span", attrs={"id":"productTitle"}).string.strip()
        except AttributeError:
            name = ""	
        return name

    # Extract product price
    def get_amazon_product_price(self):
        price = self.get_price_template1()
        if(price==""):
            price = self.get_price_template2()
        
        currency_code = "USD"

        # convert to float
        price = float(re.findall("\d+\.\d+", price.replace(",", ""))[0])

        return { "price": price, "currency_code": currency_code}

    # Extract product image url
    def get_amazon_product_image(self):
        image_url = ""
        image_url = self.get_image_url_template1()
        if(image_url==""):
            image_url = self.get_image_url_template2()
        return image_url


    # Templating
    def get_price_template1(self):
        try:
            price = self.soup.find("span", attrs={"id":"kindle-price"}).string.strip()
        except AttributeError:
            price = ""
        return price

    def get_price_template2(self):
        try:
             price = self.soup.find("span", attrs={"class":"a-offscreen"}).string.strip()
        except AttributeError:
            price = ""
        return price

    def get_image_url_template1(self):
        image_url = ""
        try:
            image_container = self.soup.find("div", attrs={"id":"ebooks-main-image-container"})
            image = image_container.find("img", alt=True)["src"]

        except AttributeError:
            image_url = ""	
        return image_url

    def get_image_url_template2(self):
        image_url = ""
        try:
            image_container = self.soup.find("div", attrs={"id":"main-image-container"})
            image_url = image_container.find("img", alt=True)["src"]

        except AttributeError:
            image_url = ""	
        return image_url