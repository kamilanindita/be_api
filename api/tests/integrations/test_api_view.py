from rest_framework.test import APITestCase
from rest_framework import status
from ...models import Product
from rest_framework.test import APIClient
import time

class ScrapApiView(APITestCase):
    def test_scrap_amazon(self):
        print("sleep for 5 seconds to avoid the rate limit amazon during the testing")
        time.sleep(5)
        payload = {
            "url": "https://www.amazon.com/Logitech-C920x-Pro-HD-Webcam/dp/B085TFF7M1/ref=sr_1_6?qid=1675587192&s=computers-intl-ship&sr=1-6"
        }
        res = self.client.post("/api/scrap", payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["name"], "Logitech C920x HD Pro Webcam, Full HD 1080p/30fps Video Calling, Clear Stereo Audio, HD Light Correction, Works with Skype, Zoom, FaceTime, Hangouts, PC/Mac/Laptop/Macbook/Tablet - Black")
        self.assertEqual(res.data["price"], 63.38)
        self.assertEqual(res.data["currency_code"], "USD")
        self.assertEqual(res.data["image_url"], "https://m.media-amazon.com/images/I/71iNwni9TsL.__AC_SX300_SY300_QL70_ML2_.jpg")


    def test_scrap_ebay(self):
        payload = {
            "url": "https://www.ebay.com/itm/175541094952?hash=item28df108a28:g:6~YAAOSwW5ljoXxp&amdata=enc%3AAQAHAAAA0P%2BFL6vRD5keAb86VjsuoremxOCIS17qg4qJuURlUbLM02ahhNE3mEQaRZ11xqFarTcqOhTzqTVYifeESSxvizfXIOn76tk8JHr81pshY%2FRwaE9Yo%2FDRd9sfE3e01ETLix0gYy0pwGHTjydrwo4VqB3nqeHtda9x4eEtsFELvVSVcJENB%2BSHHxfjLJRiWpgm14lnW9jWDrB9ULF3FimSQuaD9B3hrJ4lvJ8avlr%2F69eTHv8yPvnmrLSq7hKMjDaDzwJDQ5ieZhbYV0t2H%2BWiPNw%3D%7Ctkp%3ABFBM_OiCjcRh"
        }
        res = self.client.post("/api/scrap", payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["name"], "TL electric guitar high quality basswood Body maple neck custom 6 string Guitar")
        self.assertEqual(res.data["price"], 210.00)
        self.assertEqual(res.data["currency_code"], "USD")
        self.assertEqual(res.data["image_url"], "https://i.ebayimg.com/images/g/6~YAAOSwW5ljoXxp/s-l500.jpg")


class ScrappedTotalProductGrupBy(APITestCase):
    def setUp(self):
        Product.objects.create(name="product name test amazon 1",price=10.99, currency_code="USD", image_url="https://", url_site="https://www.amazon.com", marketplace="amazon", created_at="2023-02-03")
        Product.objects.create(name="product name test amazon 2",price=11.99, currency_code="USD", image_url="https://", url_site="https://www.amazon.com", marketplace="amazon", created_at="2023-02-03")
        Product.objects.create(name="product name test amazon 3",price=12.99, currency_code="USD", image_url="https://", url_site="https://www.amazon.com", marketplace="amazon", created_at="2023-02-04")
        Product.objects.create(name="product name test ebay 1",price=15.69, currency_code="USD", image_url="https://", url_site="https://www.ebay.com", marketplace="ebay", created_at="2023-02-03")
        Product.objects.create(name="product name test ebay 2",price=16.69, currency_code="USD", image_url="https://", url_site="https://www.ebay.com", marketplace="ebay", created_at="2023-02-03")


    def test_get_total_order_by_marketplace(self):
        res = self.client.get("/api/scrapped/total")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]["marketplace"], "amazon")
        self.assertEqual(res.data[0]["total"], 3)
        self.assertEqual(res.data[1]["marketplace"], "ebay")
        self.assertEqual(res.data[1]["total"], 2)
    
    # def test_get_total_order_by_marketplace_and_date(self):

    # def test_get_total_order_by_marketplace_and_range_date(self):

    # def test_get_total_order_by_marketplace_and_month(self):