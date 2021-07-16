class OrderModel:
    
    def __init__(self, id, date, paid, shipped, user):
        """OrderModel constructor

        Args:
            id (int): database id
            date (string): 
            paid (int): 0 for no, 1 for yes
            shipped (int): 0 for no, 1 for yes
            user (int): user id
        """
        self.id = id
        self.date = date
        self.paid = paid
        self.shipped = shipped
        self.user = user