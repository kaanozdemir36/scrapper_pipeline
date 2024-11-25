from datetime import datetime
from config.db_config import get_database

db = get_database()
collection = db['products']


def upsert_product(product):
    query = {"stock_code": product.stock_code}
    update = {
        "$set": {
            "name": product.name,
            "images": product.images,
            "price": product.price,
            "discounted_price": product.discounted_price,
            "product_type": product.product_type,
            "quantity": product.quantity,
            "color": product.color,
            "series": product.series,
            "season": product.season,
            "description": product.description,
            "is_discounted": product.is_discounted,
            "updatedAt": datetime.now()
        }
    }
    collection.update_one(query, update, upsert=True)
