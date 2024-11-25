import unittest
from models.product import Product
from services.product_service import upsert_product


class TestProductService(unittest.TestCase):
    def test_upsert_product(self):
        sample_product = {
            "ProductId": "12345",
            "Name": "Kaan Test Product",
            "Images": ["image1.jpg", "image2.jpg"],
            "Details": {
                "Price": "5.24",
                "DiscountedPrice": "4.24",
                "ProductType": "Type A",
                "Quantity": "10",
                "Color": "Blue",
                "Series": "1M-1L-1XL",
                "Season": "2024 Yaz",
            },
            "Description": "Test Description"
        }
        product = Product(sample_product)
        upsert_product(product)
