"""
Inventory Management System
---------------------------
This module provides basic functions to add, remove, load, save, and
display inventory items with quantities. It demonstrates best practices
for logging, error handling, and file operations.
"""

import json
import logging
from datetime import datetime

# --------------------------- Logging Configuration --------------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# --------------------------- Global Data Structure --------------------------- #
stock_data = {}


# --------------------------- Inventory Functions --------------------------- #
def add_item(item: str = "default", qty: int = 0, logs=None):
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []

    # Validate input
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid item or quantity type: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %s of %s", qty, item)


def remove_item(item: str, qty: int):
    """Remove a quantity of an item from the inventory."""
    try:
        if item not in stock_data:
            logging.warning("Tried to remove %s, but it doesn't exist.", item)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("%s removed from stock.", item)
        else:
            logging.info("Removed %s of %s. Remaining: %s", qty, item, stock_data[item])
    except KeyError as err:
        logging.error("Error removing item: %s", err)
    except Exception as err:
        logging.exception("Unexpected error removing item: %s", err)


def get_qty(item: str) -> int:
    """Return the quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file_name: str = "inventory.json"):
    """Load inventory data safely from a JSON file."""
    global stock_data
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
        logging.info("Loaded data from %s", file_name)
    except FileNotFoundError:
        logging.warning("%s not found. Starting with empty inventory.", file_name)
        stock_data = {}
    except json.JSONDecodeError as err:
        logging.error("Invalid JSON in %s: %s", file_name, err)


def save_data(file_name: str = "inventory.json"):
    """Save inventory data safely to a JSON file."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
        logging.info("Data saved to %s", file_name)
    except Exception as err:
        logging.exception("Failed to save data: %s", err)


def print_data():
    """Display all inventory items and quantities."""
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: int = 5):
    """Return a list of items whose quantity is below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


# --------------------------- Main Execution --------------------------- #
def main():
    """Run sample inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, now caught by validation
    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()

    # Removed eval() — no unsafe code execution here
    logging.info("Program executed successfully.")


if __name__ == "__main__":
    main()
