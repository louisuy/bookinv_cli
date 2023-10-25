# Book Inventory Management System

This is a simple command-line-based book inventory management system, created as a skills review during a job interview. It allows users to add, sell, and check the stock of books efficiently, all while storing data in a CSV file.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Optimizations](#optimizations)

## Features

- **Add Books:** Add new books to your inventory, including title, author, ISBN, price, and stock quantity. If a book with the same ISBN already exists, you can choose to add more stock.

- **Sell Books:** Deduct the quantity of a book from stock when it's sold. If the stock becomes empty, the book entry is retained in the inventory.

- **Check Stock:** Check the current stock of a book in your inventory by providing its ISBN.

- **Data Storage:** Books and inventory data are stored in a CSV file for easy retrieval and management.

## Getting Started

### Prerequisites

- Python (version 3.x)
- Basic knowledge of the command line

### Installation

1. Clone this repository or download the source code.

2. Ensure you have Python installed.

3. Run the program by executing the `bookinv.py` script.

```bash
python bookinv.py
```

## Usage

1. Upon running the program, you'll be presented with a menu-driven interface.

2. Choose an option by entering the corresponding number:

   - `1`: Add a new book to the inventory or update stock if the book already exists.
   - `2`: Sell books by specifying the book's ISBN and the quantity to sell.
   - `3`: Check the current stock of a book by providing its ISBN.
   - `4`: Exit the program.

3. Follow the prompts for each option.

## Optimizations

This program is a basic implementation. Consider the following optimizations:

- **Error Handling:** Implement more robust error handling for file operations and input validation.
- **Data Validation:** Add more data validation for various input fields.
- **Data Storage:** Depending on the scale, consider using a more scalable data storage solution like a database.
- **User Interface:** Enhance the command-line interface for a better user experience.
- **Logging:** Implement logging for debugging and auditing.
