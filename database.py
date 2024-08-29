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

def get_next_transaction_id():
    """Get the next transaction ID."""
    transactions = load_transactions()
    if not transactions:
        return 1
    return max(t['id'] for t in transactions) + 1
