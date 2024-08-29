# Copyright 2024 Giovanni Peyo
#
# This code was created with love and passion by Giovanni Peyo.
# Feel free to use and modify it for personal or educational purposes.
# Redistribution or commercial use requires explicit permission from the author.
#
# Project: Personal Finance Tracker
# Description: A simple Python application to manage personal finances.
# Created by: Giovanni Peyo


from finance import load_transactions


def generate_report():
    """Generate a financial report from transactions."""
    transactions = load_transactions()

    if not transactions:
        print("No transactions found to generate report.")
        return

    total_income = sum(t['amount'] for t in transactions if t['category'].lower() == 'income')
    total_expenses = sum(t['amount'] for t in transactions if t['category'].lower() != 'income')
    balance = total_income - total_expenses

    print("\n--- Financial Report ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")
    print("------------------------\n")
