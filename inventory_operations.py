# inventory_operations.py
# Name: Chloé Marie Mitellus
# Student ID: 125390933
# Date: 3/4/26
# Description: Inventory operations module.

"""
Inventory operations module.

This module contains all menu handler functions for inventory management.
These functions interact with Product and Inventory objects.

ADAPTED FROM A3: Replace TODO sections to use class methods instead of 
dictionary operations.
"""

import transaction_operations


# =============================================================================
# MENU HANDLER FUNCTIONS (ADAPT FROM A3)
# =============================================================================
# These functions are based on the A3 code.
# UPDATE the marked TODO sections to use Product and Inventory class methods.

def view_all_products_menu(inventory):
    """Display all products in formatted table."""
    print("\n--- All Products ---")
    
    # TODO A4: Replace dictionary access with Inventory method
    products = inventory.get_all_products()  # TODO: Get all products from inventory
    
    if not products:
        print("No products in inventory.")
        return
    
    # Print header (REUSABLE)
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10} {'Min Stock':<10}")
    print("=" * 71)
    
    # TODO A4: Replace dictionary access with Product properties
    for product in products:
        # TODO: Update this print statement to use Product properties
        print(f"{product.product_id:<6} {product.name:<20} {product.category:<15} €{product.price:<9.2f} {product.quantity:<10} {product.min_stock:<10}")
    
    print("=" * 71)
    print(f"Total products: {len(inventory)}")


def add_product_menu(inventory, transactions):
    """Add a new product to inventory."""
    print("\n--- Add New Product ---")
    
    # Get product name (REUSABLE - no changes needed)
    name = input("Enter product name: ").strip()
    
    # TODO A4: Replace dictionary loop with Inventory method
    if inventory.find_by_name(name) is not None:
        return None
    # Check if product name already exists

    
    # Get remaining details (REUSABLE - no changes needed)
    from main import get_valid_float, get_valid_int
    category = input("Enter category: ").strip()
    price = get_valid_float("Enter price (€): ", min_value=0.01)
    qty = get_valid_int("Enter current stock quantity: ", min_value=0)
    min_stock = get_valid_int("Enter minimum stock level: ", min_value=0)
    
    # TODO A4: Replace dictionary creation with Inventory method
    product_id = inventory.add_product(name,category,price,qty,min_stock)  # TODO: Add product and capture returned product ID
    
    # Log transaction (REUSABLE - no changes needed)
    transaction_operations.log_transaction(transactions, "added", product_id, name, qty)
    
    print(f"\nProduct '{name}' added successfully with ID: {product_id}")
    return product_id


def update_stock_menu(inventory, transactions):
    """Update stock for a product (sale or delivery)."""
    print("\n--- Update Stock ---")
    
    # Get product name (REUSABLE - no changes needed)
    name = input("Enter product name: ").strip()
    
    # TODO A4: Replace dictionary loop with Inventory methods
    product_id = inventory.find_by_name(name)  # TODO: Find product by name
    
    if product_id is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    product = inventory.get_product(product_id)  # TODO: Get product object
    
    # Get transaction type (REUSABLE - no changes needed)
    transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()
    
    while transaction_type not in ['s', 'd', 'sale', 'delivery']:
        print("Error: Please enter 'S' for sale or 'D' for delivery")
        transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()
    
    # Get quantity (REUSABLE - no changes needed)
    from main import get_valid_int
    quantity = get_valid_int("Enter quantity: ", min_value=1)
    
    # TODO A4: Replace dictionary update with Product method
    try:
        if transaction_type in ['s', 'sale']:
            # TODO: Update stock using Product method
            trans_type = "sale"
            change = -quantity
            product.update_stock(change)
        else:  # delivery
            # TODO: Update stock using Product method
            trans_type = "delivery"
            change = quantity
            product.update_stock(change)
        
        # Log transaction (REUSABLE - no changes needed)
        # TODO: Get product name from Product property
        transaction_operations.log_transaction(transactions, trans_type, product_id, product.name, change)  # TODO: Fix product name
        
        # TODO A4: Replace dictionary access with Product properties
        print(f"\nStock updated! {product.name} now has {product.quantity} units.")  # TODO
        return True
        
    except ValueError as e:
        print(f"Error: {e}")
        return False


def update_product_details_menu(inventory):
    """Update product details (name, category, price, min_stock)."""
    print("\n--- Update Product Details ---")
    
    # Get product name (REUSABLE - no changes needed)
    name = input("Enter product name: ").strip()
    
    # TODO A4: Replace dictionary loop with Inventory method
    product_id = inventory.find_by_name(name)  # TODO: Find product by name
    
    if product_id is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    product = inventory.get_product(product_id)  # TODO: Get product object
    
    # Display current details (REUSABLE structure, need to update access)
    # TODO A4: Replace dictionary access with Product properties
    print(f"\nCurrent details for {product.product_id}:")  # TODO
    print(f"  Name: {product.name}")  # TODO
    print(f"  Category: {product.category}")  # TODO
    print(f"  Price: €{product.price:.2f}")  # TODO
    print(f"  Min Stock: {product.min_stock}")  # TODO
    
    # Get update choice (REUSABLE - no changes needed)
    print("\nWhat would you like to update?")
    print("1. Name")
    print("2. Category")
    print("3. Price")
    print("4. Minimum Stock Level")
    print("5. Cancel")
    
    from main import get_valid_int
    choice = get_valid_int("Enter your choice (1-5): ", min_value=1)
    
    while choice not in range(1, 6):
        print("Error: Please enter a number between 1 and 5")
        choice = get_valid_int("Enter your choice (1-5): ", min_value=1)
    
    if choice == 5:
        print("Update cancelled.")
        return False
    
    # TODO A4: Replace dictionary updates with Product property setters
    try:
        if choice == 1:
            new_name = input("Enter new name: ").strip()
            # TODO: Set product name using property setter
            product.name = new_name
            print(f"\nName updated successfully to: {new_name}")
        
        elif choice == 2:
            new_category = input("Enter new category: ").strip()
            # TODO: Set product category using property setter
            product.category = new_category
            print(f"\nCategory updated successfully to: {new_category}")
        
        elif choice == 3:
            from main import get_valid_float
            new_price = get_valid_float("Enter new price (€): ", min_value=0.01)
            # TODO: Set product price using property setter
            product.price = new_price
            print(f"\nPrice updated successfully to: €{new_price:.2f}")
        
        elif choice == 4:
            new_min_stock = get_valid_int("Enter new minimum stock level: ", min_value=0)
            # TODO: Set product min_stock using property setter
            product.min_stock = new_min_stock
            print(f"\nMinimum stock level updated successfully to: {new_min_stock}")
        
        return True
        
    except ValueError as e:
        print(f"Error: {e}")
        return False


def remove_product_menu(inventory, transactions):
    """Remove a product from inventory."""
    print("\n--- Remove Product ---")
    
    # Get product name (REUSABLE - no changes needed)
    name = input("Enter product name to remove: ").strip()
    
    # TODO A4: Replace dictionary loop with Inventory method
    product_id = inventory.find_by_name(name)  # TODO: Find product by name
    
    if product_id is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    # Confirm removal (REUSABLE - no changes needed)
    confirm = input(f"Are you sure you want to remove '{name}'? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        # TODO A4: Replace dictionary deletion with Inventory method
        removed = inventory.remove_product(product_id)  # TODO: Remove product using Inventory method
        
        if removed:
            # Log transaction (REUSABLE - no changes needed)
            # TODO: Get removed product name from Product property
            transaction_operations.log_transaction(transactions, "removed", product_id, name, 0)  # TODO: Fix product name
            print(f"\nProduct '{name}' removed successfully.")  # TODO
            return True
    else:
        print("Removal cancelled.")
        return False


def search_products_menu(inventory):
    """Search for products by name or category."""
    print("\n--- Search Products ---")
    print("1. Search by name")
    print("2. Search by category")
    
    from main import get_valid_int
    choice = get_valid_int("Enter your choice (1-2): ", min_value=1)
    
    while choice not in [1, 2]:
        print("Error: Please enter 1 or 2")
        choice = get_valid_int("Enter your choice (1-2): ", min_value=1)
    
    # TODO A4: Replace dictionary loops with Inventory search methods
    if choice == 1:
        search_term = input("Enter product name (or part of name): ").strip()
        results = inventory.search_by_name(search_term)  # TODO: Search by name using Inventory method
    else:
        category = input("Enter category: ").strip()
        results = inventory.search_by_category(category)  # TODO: Search by category using Inventory method
    
    if not results:
        print("No products found matching your search.")
        return
    
    print(f"\nFound {len(results)} product(s):\n")
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10}")
    print("=" * 61)
    
    # TODO A4: Replace dictionary access with Product properties
    for product in results:
        # TODO: Update to use Product properties
        print(f"{product.product_id:<6} {product.name:<20} {product.category:<15} €{product.price:<9.2f} {product.quantity:<10}")


def view_low_stock_menu(inventory):
    """Display products at or below minimum stock levels."""
    print("\n--- Low Stock Alerts ---")
    
    # TODO A4: Replace manual loop with Inventory method
    low_stock = inventory.get_low_stock_products()  # TODO: Get low stock products using Inventory method
    
    if not low_stock:
        print("No products are currently low on stock.")
        return
    
    print(f"Found {len(low_stock)} product(s) needing restocking:\n")
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Current':<10} {'Minimum':<10}")
    print("=" * 61)
    
    # TODO A4: Replace dictionary access with Product properties
    for product in low_stock:
        # TODO: Update to use Product properties
        print(f"{product.product_id:<6} {product.name:<20} {product.category:<15} {product.quantity:<10} {product.min_stock:<10}")


def view_category_report_menu(inventory):
    """Generate and display category report."""
    print("\n--- Category Report ---")
    
    # TODO A4: Replace manual calculation with Inventory method
    report = inventory.generate_category_report()  # TODO: Generate report using Inventory method
    
    if not report:
        print("No products in inventory.")
        return
    
    print(f"{'Category':<20} {'Count':<10} {'Total Value':<15}")
    print("=" * 45)
    
    total_products = 0
    total_value = 0.0
    
    # TODO A4: Update to use report structure from Inventory method
    for category, stats in sorted(report.items()):
        # TODO: Access count and value from stats dictionary
        print(f"{category:<20} {stats['count']:<10} €{stats['value']:<14.2f}")  # TODO
        total_products += stats['count']  # TODO
        total_value += stats['value']  # TODO
    
    print("=" * 45)
    print(f"{'TOTAL':<20} {total_products:<10} €{total_value:<14.2f}")


def view_transaction_log_menu(transactions):
    """View recent transaction history."""
    print("\n--- Transaction Log ---")
    
    if not transactions:
        print("No transactions recorded.")
        return
    
    from main import get_valid_int
    num = get_valid_int("How many recent transactions to display? (default 10): ", min_value=1)
    
    # Use transaction_operations module (REUSABLE - no changes needed)
    transaction_operations.view_transaction_log(transactions, num)
