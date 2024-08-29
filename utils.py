# Copyright 2024 Giovanni Peyo
#
# This code was created with love and passion by Giovanni Peyo.
# Feel free to use and modify it for personal or educational purposes.
# Redistribution or commercial use requires explicit permission from the author.
#
# Project: Personal Finance Tracker
# Description: A simple Python application to manage personal finances.
# Created by: Giovanni Peyo


def print_menu():
    """Print the menu options for the user."""
    print("\nPersonal Finance Tracker")
    print("-----------------------")
    print("1. Add a new transaction")
    print("2. View all transactions")
    print("3. Delete a transaction")
    print("4. Generate a report")
    print("5. Exit")
    print("-----------------------")

def validate_float(input_value):
    """Validate that the input value can be converted to a float."""
    try:
        return float(input_value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None

def validate_date(input_date):
    """Validate the date format is YYYY-MM-DD."""
    import re
    if re.match(r"\d{4}-\d{2}-\d{2}", input_date):
        return input_date
    else:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return None
