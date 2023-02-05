from django.test import TestCase
from ...models import Product

class TestProductModels(TestCase):

    def create_product(self):
        return Product.objects.create(name="product name test",price=10.99, currency_code="USD", image_url="https://", url_site="https://www.amazon.com", marketplace="amazon")

    def test_product_creation(self):
        product = self.create_product()
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(product.name, "product name test")
        self.assertEqual(product.price, 10.99)
        self.assertEqual(product.currency_code, "USD")
        self.assertEqual(product.image_url, "https://")
        self.assertEqual(product.url_site, "https://www.amazon.com")
        self.assertEqual(product.marketplace, "amazon")