# Many-to-many Object Relationships Lab

This project implements a many-to-many relationship between Books and Authors through Contracts in Python.

## Overview

This application models a system for managing book contracts between authors and publishers. It demonstrates a many-to-many relationship where:
- Authors can have many books through contracts
- Books can have many authors through contracts
- Contracts serve as the intermediary table connecting authors and books

## Features

### Author Class
- **Attributes**: `name` (string)
- **Class Attributes**: `all` (list of all Author instances)
- **Methods**:
  - `contracts()`: Returns a list of all contracts for the author
  - `books()`: Returns a list of all books the author has contracted
  - `sign_contract(book, date, royalties)`: Creates a new contract for a book
  - `total_royalties()`: Returns the total royalties earned from all contracts

### Book Class
- **Attributes**: `title` (string)
- **Class Attributes**: `all` (list of all Book instances)
- **Methods**:
  - `contracts()`: Returns a list of all contracts for the book
  - `authors()`: Returns a list of all authors with contracts for the book

### Contract Class
- **Attributes**: 
  - `author` (Author instance)
  - `book` (Book instance)
  - `date` (string)
  - `royalties` (integer)
- **Class Attributes**: `all` (list of all Contract instances)
- **Methods**:
  - `contracts_by_date(date)`: Returns all contracts with the specified date (class method)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install pipenv
   pipenv install
   ```

## Usage

```python
from lib.many_to_many import Author, Book, Contract

# Create authors
author1 = Author("Jane Austen")
author2 = Author("Mark Twain")

# Create books
book1 = Book("Pride and Prejudice")
book2 = Book("Tom Sawyer")

# Authors sign contracts for books
contract1 = author1.sign_contract(book1, "01/01/2023", 50000)
contract2 = author2.sign_contract(book2, "01/01/2023", 45000)

# Get author's books
print(author1.books())  # [book1]

# Get book's authors
print(book1.authors())  # [author1]

# Get author's total royalties
print(author1.total_royalties())  # 50000

# Get contracts by date
print(Contract.contracts_by_date("01/01/2023"))  # [contract1, contract2]
```

## Testing

Run the test suite:
```bash
python -m pytest lib/testing/test_many_to_many.py -v
```

All 14 tests should pass, validating:
- Class initialization
- Property validation
- Many-to-many relationship methods
- Contract signing and royalties calculation
- Contract filtering by date

## Project Structure

```
python-oo-many-to-many-book-contracts-lab/
├── lib/
│   ├── many_to_many.py      # Main implementation
│   └── testing/
│       ├── conftest.py      # Test configuration
│       └── test_many_to_many.py  # Test suite
├── Pipfile                  # Dependencies
├── README.md                # This file
└── pytest.ini               # Pytest configuration
```

## License

MIT License

