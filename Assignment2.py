class AvailEbooks:
    """
    Represents an available e-book with attributes like book info, author, price, category, and creation date.
    """

    def __init__(self, book_info, author, price, category, creation_date):
        # Initialize the e-book details
        self._book_info = book_info
        self._author = author
        self._price = price
        self._category = category
        self._creation_date = creation_date

    # Getters and setters for each attribute
    def get_book_info(self):
        return self._book_info

    def set_book_info(self, book_info):
        self._book_info = book_info

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def get_creation_date(self):
        return self._creation_date

    def set_creation_date(self, creation_date):
        self._creation_date = creation_date

    def __str__(self):
        # Returns a string representation of the e-book details
        return (f"Book Info: {self._book_info}\nAuthor: {self._author}\n Price: {self._price}\n"
                f"Category: {self._category}\nCreation Date: {self._creation_date}")


class List_Of_EBooks:
    def __init__(self):
        # List to hold selected e-books
        self.selection = []

    def add_books(self, ebook):
        # Adds an e-book if it's an instance of AvailEbooks
        if isinstance(ebook, AvailEbooks):
            self.selection.append(ebook)
            print(
                f"'{ebook.get_book_info()}' has been added to the selection of books.")
        else:
            raise TypeError("Only AvailEbooks instances can be added.")

    def remove_books(self, ebook_title):
        # Removes an e-book by title from the selection
        self.selection = [
            ebook for ebook in self.selection if ebook.get_book_info() != ebook_title]
        print(f"'{ebook_title}' has been removed from the selection of books.")

    def show_selection(self):
        # Displays the list of available books
        if not self.selection:
            return "No E-book matching this in our selection"
        selection_of_books = "Currently Available E-books:\n"
        for ebook in self.selection:
            selection_of_books += f"The book by {ebook.get_author()} is named {ebook.get_book_info()}, Price: {ebook.get_price()}\n"
        return selection_of_books

    # Getters and setters for selection
    def get_selection(self):
        return self.selection

    def set_selection(self, selection):
        self.selection = selection


class CustInfo:
    def __init__(self, name, email, mobile_num, address):
        # Customer details
        self._name = name
        self._email = email
        self._mobile_num = mobile_num
        self._address = address

    # Getters and setters for each attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_mobile_num(self):
        return self._mobile_num

    def set_mobile_num(self, mobile_num):
        self._mobile_num = mobile_num

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def __str__(self):
        # Returns a string representation of customer details
        return (f"Name: {self._name}\nEmail: {self._email}\nPhone Number: {self._mobile_num}\nCurrent Address: {self._address}")


class Invoice:
    """
    Represents an invoice tied to an order with transaction status and an ID.
    """

    def __init__(self, order, invoiceID, transaction_status="Pending"):
        self.order = order  # Composition: Invoice is tightly coupled to CartAndOrder
        self.transaction_status = transaction_status
        self.invoiceID = invoiceID

    # Getters and setters for each attribute
    def get_order(self):
        return self.order

    def set_order(self, order):
        self.order = order

    def get_transaction_status(self):
        return self.transaction_status

    def set_transaction_status(self, transaction_status):
        self.transaction_status = transaction_status

    def get_invoiceID(self):
        return self.invoiceID

    def set_invoiceID(self, invoiceID):
        self.invoiceID = invoiceID

    def __str__(self):
        # Returns a string representation of the invoice
        return (f"Invoice ID: {self.invoiceID}\nCustomer: {self.order.cust.get_name()}\nTransaction Status: {self.transaction_status}")


class TotalPrice:
    def __init__(self, basis_price, special_cust, amount=1):
        # Pricing details
        self._amount = amount
        self._basis_price = basis_price
        self._special_cust = special_cust
        self._special_discount = 0.1
        self._wholesale_discount = 0.2
        self._tax = 0.08

    # Getters and setters for each attribute
    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_basis_price(self):
        return self._basis_price

    def set_basis_price(self, basis_price):
        self._basis_price = basis_price

    def get_special_cust(self):
        return self._special_cust

    def set_special_cust(self, special_cust):
        self._special_cust = special_cust

    def get_tax(self):
        return self._tax

    def set_tax(self, tax):
        self._tax = tax

    def no_discount(self):
        # Calculates the price without any discounts
        return self._basis_price * (1 + self._tax)

    def apply_discounts(self):
        # Calculates the price with applicable discounts
        discount = 0
        if self._special_cust:
            discount += self._special_discount
        if self._amount >= 5:
            discount += self._wholesale_discount
        return (self._basis_price * (1 - discount)) * (1 + self._tax)

    def __str__(self):
        # String representation of the total price with and without discounts
        return (f"Basis Price: {self._basis_price} AED\nSpecial Customer: {self._special_cust}\n"
                f"Total Price (with discounts, including tax): {self.apply_discounts()} AED\n"
                f"Total Price (without discounts, including tax): {self.no_discount()} AED")


class CartAndOrder:
    def __init__(self, cust, orders, invoiceID):
        self.cust = cust
        self.orders = orders
        self.list_of_books = []
        # Set invoice with specified ID
        self.invoice = Invoice(self, invoiceID)
        self.total_price = None

    # Getters and setters for each attribute
    def get_cust(self):
        return self.cust

    def set_cust(self, cust):
        self.cust = cust

    def get_orders(self):
        return self.orders

    def set_orders(self, orders):
        self.orders = orders

    def get_list_of_books(self):
        return self.list_of_books

    def set_list_of_books(self, list_of_books):
        self.list_of_books = list_of_books

    def get_invoice(self):
        return self.invoice

    def set_invoice(self, invoice):
        self.invoice = invoice

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, basis_price, special_cust, amount=1):
        # Sets the total price with aggregation
        self.total_price = TotalPrice(basis_price, special_cust, amount)

    def add_ebook(self, ebook):
        # Adds an e-book to the cart
        self.list_of_books.append(ebook)

    def __str__(self):
        all_books = ""
        for book in self.list_of_books:
            all_books += f"Title: {book.get_book_info()}, Author: {book.get_author()}, Price: {book.get_price()}\n"
        return (f"Customer: {self.cust.get_name()}\nOrder Date: {self.orders}\nBooks in Cart:\n{all_books}\n")
