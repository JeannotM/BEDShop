class ProductModel:
    
    def __init__(self, id, code, title, description, price, category, stock):
        """ProductModel constructor

        Args:
            id (int): database id
            code (string): product-code
            title (string): 
            description (string): 
            price (int): in cents
            category (int): category id 
            stock (int): amount in stock
        """
        self.id = id
        self.code = code
        self.title = title
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category