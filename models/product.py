class Product:
    def __init__(self, product_data):
        self.stock_code = product_data.get('ProductId')
        self.name = product_data.get('Name').capitalize()
        self.images = product_data.get('Images', [])
        self.price = float(
            product_data['Details'].get('Price', '0').replace(',', '.'))
        self.discounted_price = float(
            product_data['Details'].get('DiscountedPrice', '0').replace(',', '.'))
        self.product_type = product_data['Details'].get('ProductType', '')
        self.quantity = int(product_data['Details'].get('Quantity', '0'))
        self.color = [product_data['Details'].get('Color', '').capitalize()]
        self.series = product_data['Details'].get('Series', '')
        self.description = product_data.get('Description')
        self.season = product_data.get('Season')
        self.is_discounted = self.discounted_price < self.price
