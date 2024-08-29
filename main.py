# Copyright 2024 Giovanni Peyo
#
# This code was created with love and passion by Giovanni Peyo.
# Feel free to use and modify it for personal or educational purposes.
# Redistribution or commercial use requires explicit permission from the author.
#
# Project: Personal Finance Tracker
# Description: A simple Python application to manage personal finances.
# Created by: Giovanni Peyo

from finance import add_transaction, view_transactions, delete_transaction
from report import generate_report
from utils import print_menu

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add a new transaction
            category = input("Enter category (e.g., Income, Food, Rent): ").strip()
            amount = input("Enter amount: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            description = input("Enter description: ").strip()

            add_transaction(category, amount, date, description)

        elif choice == '2':
            # View all transactions
            view_transactions()

        elif choice == '3':
            # Delete a transaction
            transaction_id = input("Enter the transaction ID to delete: ").strip()
            delete_transaction(transaction_id)

        elif choice == '4':
            # Generate a report
            generate_report()

        elif choice == '5':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
