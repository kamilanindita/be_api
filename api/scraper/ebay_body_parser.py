import re
class EbayBodyParser:
    def __init__(self, soup):
        self.soup = soup

    def get_ebay_extract(self):
        name = self.get_ebay_product_name()
        product_price = self.get_ebay_product_price()
        image_url = self.get_ebay_product_image()

        return {
            "name": name,
            "price": product_price["price"],
            "currency_code": product_price["currency_code"],
            "image_url": image_url,
            "marketplace": "ebay"
        }

    # Extract product name/title
    def get_ebay_product_name(self):
        name = ""
        name = self.get_name_template1()
        if(name==""):
            name = self.get_name_template2()
            
        return name.strip()

    # Extract product price
    def get_ebay_product_price(self):
        price = ""
        price = self.get_price_template1()
        if(price==""):
            price = self.get_price_template2()

        if(price==""):
            price = self.get_price_template3()

        # get currency_code
        currency_code = price.split(" ")[0] + "D"
        # convert to float
        price = float(re.findall("\d+\.\d+", price.replace(",", ""))[0])

        return { "price": price, "currency_code": currency_code}

    # Extract product image url
    def get_ebay_product_image(self):
        image_url = ""
        image_url = self.get_image_url_template1()
        if(image_url==""):
            image_url = self.get_image_url_template2()
        return image_url


    # Templating
    def get_name_template1(self):
        name = ""
        try:
            name = self.soup.find("h1", attrs={"class": "x-item-title__mainTitle"}).text
        except AttributeError:
            name = ""
        return name

    def get_name_template2(self):
        name = ""
        try:
            name = self.soup.find("h1", attrs={"class": "product-title"}).text
        except AttributeError:
            name = ""
        return name

    def get_price_template1(self):
        price = ""
        try:
            price = self.soup.find("div", attrs={"class":"x-price-primary"}).text
        except AttributeError:
            price = ""
        return price

    def get_price_template2(self):
        price = ""
        try:
            price = self.soup.find("div", attrs={"class":"original-price"}).text
        except AttributeError:
            price = ""
        return price

    def get_price_template3(self):
        price = ""
        # try:
        #     # price = self.soup.findAll("span")

        # except AttributeError:
        #     price = ""
        return price

    def get_image_url_template1(self):
        image_url = ""
        try:
            image_url = self.soup.find("div", attrs={"class":"ux-image-carousel-item active image"}).find("img", alt=True)["src"]
        except AttributeError:
            image_url = ""
        return image_url

    def get_image_url_template2(self):
        image_url = ""
        try:
            image_url = self.soup.find("div", attrs={"class":"galleryPicturePanel"}).find("img", alt=True)["src"]
        except AttributeError:
            image_url = ""
        return image_url