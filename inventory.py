# inventory.py
# Name: Chloé Marie Mitellus
# Student ID: 125390933
# Date: 24/3/26
# Description: Contains the Inventory method.

from product import Product

class Inventory:

    def __init__(self):
        self._products = {}

    def add_product(self ,name, category, price, quantity, min_stock):
        """
            Add a new product to the inventory.

            Parameters:
                name, category, price, quantity, min_stock (string): each given separately


            Returns:
                str or None: Product ID if successful, None if duplicate found
            """
        pid = self._generate_id()
        if self.find_by_name(name):
            return None
        self._products[pid] = Product(pid, name, category,price, quantity, min_stock )
        return pid

    def remove_product(self,product_id):
        """
            Remove a product from the inventory after confirmation.

            Returns:
                Removed Product object or None if not found
            """
        return self._products.pop(product_id,None)


    def get_product(self,product_id):
        """
        Finds a product from the inventory using the product's ID.

        Returns:
            Finds Product object or None if not found
        """
        return self._products.get(product_id,None)


    def get_all_products(self):
        """
            Finds a product from the inventory using the product's ID.

            Returns:
                List of all Product objects
        """
        prod_list = []
        for prod in self._products.values():
            prod_list.append(prod)
        return prod_list


    def find_by_name(self,name):
        """
            Search for products whose name is the same as the search term (case-insensitive).

                Parameters:
                    name (str): The term to search for

                Returns:
                    product_id or None if not found
                   """

        name = name.lower()
        for pid, prod in self._products.items():
            if prod.name.lower() == name:
                return pid

        return None


    def search_by_name(self,search_term):
        """
            Search for products whose name contains the search term (case-insensitive).

            Parameters:
                search_term (str): The term to search for

            Returns:
                List of matching Product objects
            """
        matches = []
        search_lower = search_term.lower()

        for product_id, product in self._products.items():
            if search_lower in product.name.lower():
                matches.append(product)

        return matches

    def search_by_category(self,category):
        """
            Find all products in a specific category (case-insensitive exact match).

            Parameters:
                category (str): The category to search for

            Returns:
                List of matching Product objects
        """
        matches = []
        category_lower = category.lower()

        for product_id, product in self._products.items():
            if product.category.lower() == category_lower:
                matches.append(product)
        return matches

    def get_low_stock_products(self):
        """
            Display products that are at or below their minimum stock level.

            Returns:
                List of Product objects where is_low_stock() is True
            """
        low_stock_products = []
        for product_id, product in self._products.items():
            if product.is_low_stock():
                low_stock_products.append( product)
        return low_stock_products


    def generate_category_report(self):
        """
        Creates a dictionary to be used to generate a category report.

        Returns:
            Dictionary with category statistics
            For each category: product count and total value"""
        statistics = {}
        for product in self._products.values():
            cat = product.category
            if cat not in statistics:
                statistics[cat] = {"count": 0, "value": 0.0}
            statistics[cat]["count"] += 1
            statistics[cat]["value"] += product.get_value()
        return statistics


    def calculate_total_value(self):
        """
           Calculate the total value of all inventory (price × quantity).

           Returns:
               float: Total inventory value
           """
        if not self._products:
            return 0.0

        total = 0.0
        for product in self._products.values():
            total += product.get_value()
        return total

    def _generate_id(self):
        """
           Generate the next unique product ID (P001, P002, P003, etc.).

            Returns:
                str: Next product ID in format P001, P002, etc.
        """
        if not self._products:
            return "P001"

        max_num = 0
        for product_id in self._products.keys():

            num = int(product_id[1:])
            if num > max_num:
                max_num = num


        next_num = max_num + 1
        return f"P{next_num:03d}"

    def __len__(self):
        """
        Returns:
            Number of products in inventory
            Allows using len(inventory)"""

        return len(self._products)
