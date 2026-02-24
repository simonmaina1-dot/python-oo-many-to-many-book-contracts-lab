class Author:
    """
    Author class represents an author in the book-contract system.
    Authors can have many books through contracts.
    """
    
    # Class attribute to store all Author instances
    all = []
    
    def __init__(self, name):
        """
        Initialize an Author with a name.
        
        Args:
            name (str): The name of the author
        """
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        """
        Return a list of all contracts associated with this author.
        
        Returns:
            list: List of Contract instances for this author
        """
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """
        Return a list of all books associated with this author through contracts.
        
        Returns:
            list: List of Book instances
        """
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """
        Create and return a new Contract between this author and the specified book.
        
        Args:
            book (Book): The book to create a contract for
            date (str): The date of the contract
            royalties (int): The royalties amount
            
        Returns:
            Contract: The newly created contract
        """
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """
        Return the total amount of royalties earned from all contracts.
        
        Returns:
            int: Sum of all royalties from contracts
        """
        return sum(contract.royalties for contract in self.contracts())


class Book:
    """
    Book class represents a book in the book-contract system.
    Books can have many authors through contracts.
    """
    
    # Class attribute to store all Book instances
    all = []
    
    def __init__(self, title):
        """
        Initialize a Book with a title.
        
        Args:
            title (str): The title of the book
        """
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        """
        Return a list of all contracts associated with this book.
        
        Returns:
            list: List of Contract instances for this book
        """
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """
        Return a list of all authors associated with this book through contracts.
        
        Returns:
            list: List of Author instances
        """
        return [contract.author for contract in self.contracts()]


class Contract:
    """
    Contract class represents a contract between an author and a book.
    This is the intermediary table in the many-to-many relationship.
    """
    
    # Class attribute to store all Contract instances
    all = []
    
    def __init__(self, author, book, date, royalties):
        """
        Initialize a Contract with author, book, date, and royalties.
        
        Args:
            author (Author): The author instance
            book (Book): The book instance
            date (str): The date of the contract
            royalties (int): The royalties amount
            
        Raises:
            Exception: If author is not an Author instance
            Exception: If book is not a Book instance
            Exception: If date is not a string
            Exception: If royalties is not an integer
        """
        # Validate author is an Author instance
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author class")
        
        # Validate book is a Book instance
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book class")
        
        # Validate date is a string
        if not isinstance(date, str):
            raise Exception("date must be an instance of str")
        
        # Validate royalties is an integer
        if not isinstance(royalties, int):
            raise Exception("royalties must be an instance of int")
        
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        """Get the author of the contract."""
        return self._author
    
    @property
    def book(self):
        """Get the book of the contract."""
        return self._book
    
    @property
    def date(self):
        """Get the date of the contract."""
        return self._date
    
    @property
    def royalties(self):
        """Get the royalties of the contract."""
        return self._royalties
    
    @classmethod
    def contracts_by_date(cls, date):
        """
        Return all contracts that have the same date as the specified date.
        
        Args:
            date (str): The date to filter contracts by
            
        Returns:
            list: List of Contract instances with matching dates
        """
        return [contract for contract in cls.all if contract.date == date]

