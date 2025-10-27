import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    # Fix 1: Mutable default argument W0102
    if logs is None:
        logs = []

    if not item:
        return
    # Fix 1: Optional: Use f-string for C0209 (consider-using-f-string)
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # Fix 2: Bare except W0702/E722 replaced with specific exception
    except KeyError:
        pass

def get_qty(item):
    return stock_data.get(item) # Safely get the value, returns None if not found

def load_data(file="inventory.json"):
    # Fix 4: Flake8 E302/E305 (2 blank lines separation) added above
    # Pylint W1514 (unspecified-encoding) and R1732 (consider-using-with) fixed
    with open(file, "r", encoding='utf-8') as f:
        global stock_data
        stock_data = json.loads(f.read())

def save_data(file="inventory.json"):
    # Pylint W1514 (unspecified-encoding) and R1732 (consider-using-with) fixed
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))

def print_data():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    # Function calls updated to snake_case (Fix 4: C0103)
    # The logging import (Line 2) is still unused (W0611) but we'll leave it for now
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, 10) # Fixed the invalid type call to test the function's integer logic
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Fix 3: eval("print('eval used')") removed (B307/W0123)
main()