
from django.test import TestCase
from ...serializers import RequestScrapProductSerializer, SaveScrapProductSerializer, ScrapProductResponseSerializer, TotalScrapProductSerializer

class TestRequestScrapProductSerializer(TestCase):
    def test_valid_request_scrap_serializer(self):
        req_data_scrap="https://www.amazon.com/gp/product/B0818ZZNLR?pf_rd_m=ATVPDKIKX0DER&storeType=ebooks&pageType=STOREFRONT&pf_rd_p=&pf_rd_r=VDVF7JDY0TXFJK9Z91FP&pf_rd_s=merchandised-slot-5&pf_rd_t=&ref_=dbs_f_ebk_rwt_mers_ms5_kmw_10&pf_rd_i="
        
        serializer = RequestScrapProductSerializer(data={"url": req_data_scrap})
        assert serializer.is_valid()
        assert serializer.validated_data == {"url": "https://www.amazon.com/gp/product/B0818ZZNLR?pf_rd_m=ATVPDKIKX0DER&storeType=ebooks&pageType=STOREFRONT&pf_rd_p=&pf_rd_r=VDVF7JDY0TXFJK9Z91FP&pf_rd_s=merchandised-slot-5&pf_rd_t=&ref_=dbs_f_ebk_rwt_mers_ms5_kmw_10&pf_rd_i="}
        assert serializer.data == {"url": "https://www.amazon.com/gp/product/B0818ZZNLR?pf_rd_m=ATVPDKIKX0DER&storeType=ebooks&pageType=STOREFRONT&pf_rd_p=&pf_rd_r=VDVF7JDY0TXFJK9Z91FP&pf_rd_s=merchandised-slot-5&pf_rd_t=&ref_=dbs_f_ebk_rwt_mers_ms5_kmw_10&pf_rd_i="}
        assert serializer.errors == {}

    def test_invalid_request_scrap_serializer(self):
        req_data_scrap=""
        serializer = RequestScrapProductSerializer(data={"url": req_data_scrap})
        assert not serializer.is_valid()
        assert serializer.errors == {'url': ["This field may not be blank."]}

class TestSaveScrapProductSerializer(TestCase):
    def test_valid_save_serializer(self):
        data = {
            "name": "product name test", 
            "price": 10.99, 
            "currency_code": "USD",
            "image_url": "https://",
            "url_site": "https://www.amazon.com",
            "marketplace": "amazon"
        }
        serializer = SaveScrapProductSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data == data
        assert serializer.data == data
        assert serializer.errors == {}

    def test_invalid_save_serializer(self):
        data = {
            "name": "product name test", 
            "price": "$10.99", 
            "currency_code": "USD",
            "image_url": "https://",
            "url_site": "https://www.amazon.com",
            "marketplace": "amazon"
        }

        serializer = SaveScrapProductSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors == {"price": ["A valid number is required."]}

class TestScrapProductResponseSerializer(TestCase):
    def test_valid_scrap_response_serializer(self):
        data = {
            "id": "e89b-12d3-a456-426614174000",
            "name": "product name test", 
            "price": 10.99, 
            "currency_code": "USD",
            "image_url": "https://",
            "url_site": "https://www.amazon.com",
            "marketplace": "amazon"
        }

        data_expectation = {
            "name": "product name test", 
            "price": 10.99, 
            "currency_code": "USD",
            "image_url": "https://",
            "marketplace": "amazon"
        }

        serializer = ScrapProductResponseSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data == data_expectation
        assert serializer.data == data_expectation
        assert serializer.errors == {}

    def test_invalid_scrap_response_serializer(self):
        data = {
            "id": "e89b-12d3-a456-426614174000",
            "name": "product name test", 
            "price": 10.99, 
            "currency_code": "USD",
            "image_url": "https://",
            "url_site": "https://www.amazon.com",
            "marketplace": "amazon"
        }

        data_expectation = {
            "id": "e89b-12d3-a456-426614174000",
            "name": "product name test", 
            "price": 10.99, 
            "currency_code": "USD",
            "image_url": "https://",
            "marketplace": "amazon"
        }

        serializer = ScrapProductResponseSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data != data_expectation
        assert serializer.data != data_expectation

    
    def test_valid_total_scrap_serializer(self):
        data = [
            {
                "marketplace": "amazon",
                "total": 11
            },
            {
                "marketplace": "ebay",
                "total": 12
            }
        ]


        serializer = TotalScrapProductSerializer(data=data, many=True)
        assert serializer.is_valid()
        assert serializer.validated_data == data
        assert serializer.data == data