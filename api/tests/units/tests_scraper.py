from django.test import TestCase
from ...scraper.scraper import Scraper
import time

class TestScraper(TestCase):
    def test_amazon_scraper(self):
        print("sleep for 5 seconds to avoid the rate limit amazon during the testing")
        time.sleep(5)
        url ="https://www.amazon.com/Logitech-C920x-Pro-HD-Webcam/dp/B085TFF7M1/ref=sr_1_6?qid=1675587192&s=computers-intl-ship&sr=1-6"
        scraper = Scraper(url)
        result = scraper.get_data()
        assert result["name"] == "Logitech C920x HD Pro Webcam, Full HD 1080p/30fps Video Calling, Clear Stereo Audio, HD Light Correction, Works with Skype, Zoom, FaceTime, Hangouts, PC/Mac/Laptop/Macbook/Tablet - Black"
        assert result["price"] == 63.38
        assert result["image_url"] == "https://m.media-amazon.com/images/I/71iNwni9TsL.__AC_SX300_SY300_QL70_ML2_.jpg"
        

    def test_ebay_scraper(self):
        url="https://www.ebay.com/itm/175541094952?hash=item28df108a28:g:6~YAAOSwW5ljoXxp&amdata=enc%3AAQAHAAAA0P%2BFL6vRD5keAb86VjsuoremxOCIS17qg4qJuURlUbLM02ahhNE3mEQaRZ11xqFarTcqOhTzqTVYifeESSxvizfXIOn76tk8JHr81pshY%2FRwaE9Yo%2FDRd9sfE3e01ETLix0gYy0pwGHTjydrwo4VqB3nqeHtda9x4eEtsFELvVSVcJENB%2BSHHxfjLJRiWpgm14lnW9jWDrB9ULF3FimSQuaD9B3hrJ4lvJ8avlr%2F69eTHv8yPvnmrLSq7hKMjDaDzwJDQ5ieZhbYV0t2H%2BWiPNw%3D%7Ctkp%3ABFBM_OiCjcRh"
        scraper = Scraper(url)
        result = scraper.get_data()
        assert result["name"] == "TL electric guitar high quality basswood Body maple neck custom 6 string Guitar"
        assert result["price"] == 210.0
        assert result["image_url"] == "https://i.ebayimg.com/images/g/6~YAAOSwW5ljoXxp/s-l500.jpg"

    def test_marketplace_not_available_scraper(self):
        url ="https://www.tokopedia.com"
        scraper = Scraper(url)
        result = scraper.get_data()
        assert result == "marketplace not available"
