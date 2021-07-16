class UserModel:

    def __init__(self, id, email, password, firstname, infix, lastname, street, housenumber, zipcode, city, newsletter, userrole, country):
        """UserModel constructor

        Args:
            id (int): database id
            email (string): 
            password (string): 
            firstname (string): 
            infix (string): can be emtpy
            lastname (string): 
            street (string): 
            housenumber (string): with adjective (23b)
            zipcode (string): 
            city (string): 
            newsletter (int): 1 for yes, 0 for no
            userrole (int): userrole id
            country (int): country id
        """
        self.id = id
        self.email = email
        self.password = password
        self.firstname = firstname
        self.infix = infix
        self.lastname = lastname
        self.street = street
        self.housenumber = housenumber
        self.zipcode = zipcode
        self.city = city
        self.newsletter = newsletter
        self.userrole = userrole
        self.country = country