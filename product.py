# product.py
# Name: Chloé Marie Mitellus
# Student ID: 125390933
# Date: 24/3/26
# Description: Contains the Product method

class Product:
    def __init__(self,product_id, name, category, price, quantity, min_stock):
        """Initialising values"""
        self.__product_id =product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.min_stock =min_stock

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def min_stock(self):
        return self.__min_stock

    @name.setter
    def name(self, __name):
        """
        Variable __name validation

        Parameter:
            private variable __name

        Returns:
            __name with no empty or whitespace

        """
        name = __name.strip()
        if name=="":
            raise ValueError("Name can not be empty or only whitespace")
        self.__name=name

    @category.setter
    def category(self, __category):
        """
        Variable __category validation

        Parameter:
            private variable __category

        Returns:
            __category with no empty or whitespace

                """
        cat = __category.strip()
        if cat == "":
            raise ValueError("Category can not be empty or only whitespace")
        self.__category = cat

    @price.setter
    def price(self, value):
        """
        Variable value validation

        Parameter:
            value (float)

        Returns:
            __price with no negative numbers
        """
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @quantity.setter
    def quantity(self, value):
        """
        Variable value validation

        Parameter:
            value (int)

        Returns:
            __quantity with no negative numbers
        """
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    @min_stock.setter
    def min_stock(self, value):
        """
        Variable value validation

        Parameter:
            value (int)

        Returns:
            __min_stock with no negative numbers
        """
        if value < 0:
            raise ValueError("Minimum Stock cannot be negative.")
        self.__min_stock = value

    def update_stock(self, amount_change):
        """
        Update the stock quantity

        Parameters:
            amount_change (int) - amount to add (positive) or remove (negative)
        Returns:
             Raises ValueError if resulting quantity would be negative
             Updates quantity (private attribute)

        """
        total = amount_change + self.__quantity
        if total < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = total

    def get_value(self):
        """
        Gets the value of the price of a product.

        Returns:
            Total value of the product

        """

        total = self.__price * self.__quantity
        return total

    def is_low_stock(self):
        """
        Checks if current stock is lower than minimum stock.

        Returns:
            True if product needs reordering, False otherwise
        """
        if self.__quantity < self.__min_stock:
            return True
        else:
            return False

    def to_dict(self):
        """
        Shows current products
        Used for JSON storage

        Returns:
            Dictionary with all attributes EXCEPT product_id
        """
        return {"name": self.__name, "category": self.__category, "price": self.__price, "quantity": self.__quantity, "min_stock": self.__min_stock}

    @classmethod
    def from_dict(cls, product_id, data):
        """
        Creates a new product
        Used for loading from JSON

        Parameters:
            product_id (str) - Product ID of new product
            data (dict) - name, category, price, quantity, min_stock

        Returns:
            New Product object
        """
        name = data['name']
        category = data['category']
        price = data['price']
        quantity = data['quantity']
        min_stock = data['min_stock']

        return cls(product_id,name,category,price,quantity,min_stock)


    def __str__(self):
        """
        String with ID, name, category, price, stock levels

        Returns:
            Readable string representation of the product
        """
        return f"ID: {self.__product_id} | Name: {self.__name} | Category: {self.__category} | Price: €{self.__price:.2f} | Stock Levels: {self.__quantity} | Minimum Stock: {self.__min_stock}"



