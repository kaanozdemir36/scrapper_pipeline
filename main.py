from models.product import Product
from services.product_service import upsert_product
import xml.etree.ElementTree as ET

xml_file_path = 'data/lonca-sample.xml'

tree = ET.parse(xml_file_path)
root = tree.getroot()

for product_elem in root.findall('Product'):
    product_data = {
        'ProductId': product_elem.get('ProductId'),
        'Name': product_elem.get('Name'),
        'Images': [img.get('Path') for img in product_elem.find('Images')],
        'Details': {detail.get('Name'): detail.get('Value') for detail in product_elem.find('ProductDetails')},
        'Description': product_elem.find('Description').text.strip() if product_elem.find(
            'Description') is not None else None,
    }
    product = Product(product_data)
    upsert_product(product)

print("All products processed successfully.")
