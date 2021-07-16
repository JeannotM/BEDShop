class OrderLineModel:
    
    def __init__(self, id, product, order, amount, total_price):
        """OrderLineModel constructor

        Args:
            id (int): database id
            product (int): product id
            order (int): order id
            amount (int):
            total_price (int): in cents
        """
        self.id = id
        self.product = product
        self.order = order
        self.amount = amount
        self.total_price = total_price