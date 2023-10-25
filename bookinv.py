"""
Coding Exercise: Simple Inventory Management System

Objective:
Your task is to design a basic inventory management system for a small book store using object-oriented programming. This system will be able to handle new book arrivals, book sales, and checking the current inventory status.

Requirements:

Book Class:
    Each book should be an object of the 'Book' class.
    Attributes should include title (string), author (string), ISBN (string), price (float), and stock_quantity (integer).

Inventory Class:
    This class will manage the collection of books.
    Methods should include add_book (add a book to the inventory), sell_book (decrease the quantity of a book in stock), and check_stock (check the current quantity in stock for a book).

Functionalities:
1a) add_book: When a new book arrives, add it to the inventory. 
1b) If the book already exists (matched by ISBN), increase the stock_quantity instead of creating a new entry.
2) sell_book: When a book is sold, reduce its stock_quantity by the amount sold. Ensure that you handle cases where the requested amount for sale exceeds the stock_quantity.
3) check_stock: Given a book's ISBN, print out the title, author, and current stock_quantity.

Purpose: 
The purpose of this test is to just view your thought process and some coding skills.

Platform: 
You can choose any platform / tool / programming language (CLI, App, web or desktop programming).

Coding style: 
Your code should be cleanly written, well-commented, and easy to read.
Include basic error handling for real-world scenarios, like attempting to add/sell a book that doesn't exist in the inventory.

Bonus:
Implement a simple user interface through the command line / web interface / app interface for interaction with your system or a method to read inputs from a text file for bulk processing.

Submission:
1) Please submit your code file along with a brief explanation of your design and logic.
2) Include any instructions necessary for running your program.
3) make a video of your working program which covers all the given scenarios(Functionality 1a, 1b 2 & 3).
4) you have 3 days(from test receiving time) to submit the full working solution. 

Good Luck & Happy Coding."""

import csv
import re

class Book:
    def __init__(self, title, author, isbn, price, stock_quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.stock_quantity = stock_quantity

class Inventory:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.books = self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.csv_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                return [Book(**row) for row in reader]
        except FileNotFoundError:
            return []

    def save_inventory(self):
        with open(self.csv_file, 'w', newline='') as csvfile:
            fieldnames = ["title", "author", "isbn", "price", "stock_quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([vars(book) for book in self.books])

    def add_book(self, book):
        existing_book = next((b for b in self.books if b.isbn == book.isbn), None)
        if existing_book:
            existing_book.stock_quantity += book.stock_quantity
        else:
            self.books.append(book)
        self.save_inventory()

    def sell_book(self, isbn, quantity):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book:
            current_stock = int(book.stock_quantity)
            if current_stock >= quantity:
                current_stock -= quantity
                book.stock_quantity = str(current_stock)
                # FEATURE REMOVED - Books are not removed from the list when stock is depleted to avoid extra work.
                # if current_stock == 0:
                #     # Remove the book from the list when stock is depleted
                #     self.books.remove(book)
                self.save_inventory() 
            else:
                print(f"Error: Not enough stock for {book.title}. Current stock: {current_stock}")
        else:
            print("Error: Book not found in inventory.")

    def check_stock(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        if book:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Current Stock: {book.stock_quantity}")
        else:
            print("Error: Book not found in inventory.")

my_inventory = Inventory("inventory.csv")

def is_valid_isbn(isbn):
    # ISBN-10 or ISBN-13 regex pattern validation.
    isbn_pattern = r"^(?:\d[- ]?){9}[\dXx]$|^(?:\d[- ]?){13}$"
    return re.match(isbn_pattern, isbn)

def get_valid_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            if input_type == "float":
                user_input = float(user_input)
            elif input_type == "int":
                user_input = int(user_input)
            elif input_type == "isbn":
                if not is_valid_isbn(user_input):
                    raise ValueError("Invalid ISBN format")
            return user_input
        except ValueError as e:
            print("Invalid input:", e)


while True:
    option = input("Book Inventory Management System\n1.) Add Book\n2.) Sell Book\n3.) Check Stock\n4.) Exit\n\nChoose an option: ")
    match option:
        case "1":
            isbn = get_valid_input("Enter the ISBN: ", "isbn")
        
            existing_book = next((b for b in my_inventory.books if b.isbn == isbn), None)
            if existing_book:
                print("\nA book with the same ISBN already exists:\n")
                print(f"Title: {existing_book.title}")
                print(f"Author: {existing_book.author}")
                print(f"Price: {existing_book.price}")
                print(f"Current Stock: {existing_book.stock_quantity}\n")
                add_stock = get_valid_input("Enter the quantity to be added (or 0 if no new stock to be added): ", "int")
                
                if add_stock > 0:
                    existing_book.stock_quantity = str(int(existing_book.stock_quantity) + add_stock)
                    my_inventory.save_inventory()
            else:
                title = input("Enter the title: ")
                author = input("Enter the author: ")
                price = get_valid_input("Enter the price: ", "float")
                stock_quantity = get_valid_input("Enter the stock quantity: ", "int")
                book = Book(title, author, isbn, price, stock_quantity)
                my_inventory.add_book(book)
        case "2":
            isbn = get_valid_input("Enter the ISBN of the book to sell: ", "isbn")
            quantity = int(get_valid_input("Enter the quantity to sell: ", "int"))
            my_inventory.sell_book(isbn, quantity)
        case "3":
            isbn = input("Enter the ISBN of the book to check: ")
            my_inventory.check_stock(isbn)
        case "4":
            break
        case _:
            print("Invalid option. Please try again.")
    input("Press Enter to continue...")
    print("\n\n")
