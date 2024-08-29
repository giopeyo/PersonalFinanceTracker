# Copyright 2024 Giovanni Peyo
#
# This code was created with love and passion by Giovanni Peyo.
# Feel free to use and modify it for personal or educational purposes.
# Redistribution or commercial use requires explicit permission from the author.
#
# Project: Personal Finance Tracker
# Description: A simple Python application to manage personal finances.
# Created by: Giovanni Peyo


import json
from datetime import datetime

DATABASE_FILE = 'transactions.json'


def load_transactions():
    """Load transactions from the JSON file."""
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_transactions(transactions):
    """Save transactions to the JSON file."""
    with open(DATABASE_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)


def add_transaction(category, amount, date, description):
    """Add a new transaction to the list."""
    transactions = load_transactions()

    # Create a unique ID for the transaction
    transaction_id = len(transactions) + 1

    # Create a transaction record
    transaction = {
        'id': transaction_id,
        'category': category,
        'amount': float(amount),
        'date': date,
        'description': description
    }

    transactions.append(transaction)
    save_transactions(transactions)
    print(f"Transaction added successfully: {transaction}")


def view_transactions():
    """View all transactions."""
    transactions = load_transactions()
    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print(
            f"ID: {transaction['id']}, Category: {transaction['category']}, Amount: {transaction['amount']}, Date: {transaction['date']}, Description: {transaction['description']}")


def delete_transaction(transaction_id):
    """Delete a transaction by its ID."""
    transactions = load_transactions()
    new_transactions = [t for t in transactions if t['id'] != int(transaction_id)]

    if len(new_transactions) == len(transactions):
        print(f"No transaction found with ID: {transaction_id}")
        return

    save_transactions(new_transactions)
    print(f"Transaction with ID {transaction_id} deleted successfully.")
