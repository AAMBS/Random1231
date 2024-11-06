class AvailEbooks:
    def __init__(self, book_info, author, price, category, creation_date):  # Attributes for the book
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

    def __str__(self):  # Method to return string representation of the book details
        return (f"Book Info: {self._book_info}\nAuthor: {self._author}\n Price: {self._price}\nCategory: {self._category}\nCreation Date: {self._creation_date}")


class List_Of_EBooks:
    def __init__(self):
        self.selection = []  # Initializes an empty list to hold selected e-books

    def add_books(self, ebook):
        # Check if the item being added is an instance of AvailEbooks
        if isinstance(ebook, AvailEbooks):
            self.selection.append(ebook)
            print(
                f"'{ebook.get_book_info()}' has been added to the selection of books.")
        else:
            # Raise error if wrong type is added
            raise TypeError("Only AvailEbooks instances can be added.")

    def remove_books(self, ebook_title):
        for z in self.selection:
            if z.get_book_info() == ebook_title:  # Check if the book title matches
                self.selection.remove(z)  # Remove book from selection
                print(
                    f"'{ebook_title}' has been removed from the selection of books.")
                return
        # Notify if book was not found
        print(f"'{ebook_title}' is not in the selection of books.")

    def show_selection(self):
        if not self.selection:
            return "No E-book matching this in our selection"  # Notify if selection is empty

        selection_of_books = "Currently Available E-books:\n"
        for y in self.selection:
            selection_of_books += f"The book by {y.get_author()} is named {y.get_book_info()}, Price: {y.get_price()}\n"
        return selection_of_books  # Return the list of selected e-books


class CustInfo:
    def __init__(self, name, email, mobile_num, address):  # Attributes for customer information
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

    def __str__(self):  # Method to return string representation of customer details
        return (f"Name: {self._name}\nEmail: {self._email}\n Phone Number: {self._mobile_num}\nCurrent Address: {self._address}")


class CartAndOrder:
    def __init__(self, cust, orders):  # Attributes for the cart and order
        self.cust = cust  # Association with CustInfo
        self.orders = orders
        self.list_of_books = []  # List to hold books in the cart
        self.quan_orders = 0  # Counter for quantity of orders

    # Getters and setters

    def get_orders(self):
        return self.orders

    def set_orders(self, orders):
        self.orders = orders

    def add_ebook(self, ebook):  # Method to add an e-book to the cart
        self.list_of_books.append(ebook)
        self.quan_orders += 1  # Increment order quantity

    def remove_from_cart(self, ebook):  # Method to remove an e-book from the cart
        self.list_of_books.remove(ebook)
        self.quan_orders -= 1  # Decrement order quantity
        return f"The {ebook.get_book_info()} has been deleted from cart."

    def __str__(self):  # Method to return string representation of cart contents
        books_str = ""
        for x in self.list_of_books:
            books_str += f"Title: {x.get_book_info()}, Author: {x.get_author()}, Price: {x.get_price()}\n"
        return (f"Customer: {self.cust.get_name()}\nOrder Date: {self.orders}\n Quantity of Orders: {self.quan_orders}\nBooks in Cart:\n{books_str}")


class Invoice:
    def __init__(self, order, transaction_status, invoiceID):  # Attributes for the invoice
        self.order = order
        self.transaction_status = transaction_status
        self.invoiceID = invoiceID

    def __str__(self):  # Method to return string representation of invoice details
        return (f"Invoice ID: {self.invoiceID}\nCustomer: {self.order.cust.get_name()}\n"
                f"Transaction Status: {self.transaction_status}")


class TotalPrice:
    # Attributes for pricing calculations
    def __init__(self, basis_price, special_cust, amount=1):
        self._amount = amount                  # Number of items (books)
        self._basis_price = basis_price        # Total price of books without discounts
        self._special_cust = special_cust      # Boolean for special customer status
        self._special_discount = 0.1           # 10% special discount
        self._wholesale_discount = 0.2         # 20% wholesale discount
        self._tax = 0.08                       # 8% tax

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

    def no_discount(self):  # Method to calculate price without discounts
        total_price = self._basis_price * \
            (1 + self._tax)  # Add tax to basis price
        return total_price

    def apply_discounts(self):  # Method to calculate price with discounts
        discount = 0
        base_price = self._basis_price  # Base price of books

        if self._special_cust:  # Check if the customer is special
            discount += self._special_discount
        if self._amount >= 5:  # Check for wholesale discount
            discount += self._wholesale_discount

        if discount > 0:
            discounted_price = base_price * \
                (1 - discount)  # Calculate discounted price
        else:
            discounted_price = base_price  # No discounts

        total_price = discounted_price * \
            (1 + self._tax)  # Add tax to discounted price
        return total_price

    def __str__(self):  # Method to return string representation of total price calculations
        # Calculate price with discounts
        total_price_with_discount = self.apply_discounts()
        # Calculate price without discounts
        total_price_without_discount = self.no_discount()

        return (f"Basis Price: {self._basis_price} AED\n Special Customer: {self._special_cust}\n Total Price (with discounts, including tax): {total_price_with_discount} AED\n Total Price (without discounts, including tax): {total_price_without_discount} AED")
