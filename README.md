# Inventory-Manager

A Python-based terminal application for managing inventory, designed for Murphy's General Store. This system uses Object-Oriented Programming principles to track products, manage stock levels, log transactions, and generate formatted reports with persistent JSON storage.

## Features

* **Complete Inventory Control:** Add, remove, and update products with automatic unique ID generation (e.g., P001, P002).
* **Stock Management:** Process sales and deliveries, and automatically flag items that fall below user-defined minimum stock thresholds.
* **Search and Filter:** Look up products by exact name, partial name, or category.
* **Transaction Logging:** Keep a historical record of all inventory changes (added, removed, sales, and deliveries).
* **Reporting & Exporting:** Generate summary reports by category and total inventory value. Export data to CSV and formatted text files.
* **Data Persistence:** Automatically saves and loads inventory and transaction histories using JSON files to ensure no data is lost between sessions.

## Project Structure

* **`main.py`**: The entry point of the application containing the primary menu loop and user input validation.
* **`product.py`**: Contains the `Product` class with strict property validation (e.g., preventing negative prices or quantities) and stock calculation methods.
* **`inventory.py`**: Contains the `Inventory` class which manages a collection of `Product` objects, handling additions, removals, searches, and category report generation.
* **`inventory_operations.py`**: Handles all CLI menu interactions related to the inventory, linking user input to `Inventory` and `Product` class methods.
* **`transaction_operations.py`**: Manages the logging and displaying of the recent transaction history.
* **`data_handler.py`**: Handles persistent data storage (reading/writing to `inventory.json` and `transactions.json`) and report exportation (CSV and TXT).

## Requirements

* Python 3.x
* No external dependencies or libraries required (uses built-in `json`, `csv`, and `datetime` modules).

## Installation and Setup

1. Clone this repository to your local machine.
2. Ensure all project files are located in the same directory.
3. Open your terminal or command prompt and navigate to the project folder.
4. Run the program by executing the main script:
   ```bash
   python main.py
   ```
5. Follow the on-screen menu prompts to manage your inventory. Data will automatically save to `inventory.json` and `transactions.json` when you choose to "Save & Exit".
