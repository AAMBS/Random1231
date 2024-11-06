from Assignment2 import *  # Import all classes from Assignment2

# Print header for E-Book selection
print("--~~ E-Book Selection Management ~~--")
book_list = List_Of_EBooks()  # Create an instance of the List_Of_EBooks class

# Create instances of AvailEbooks with proper attributes
book1 = AvailEbooks("No Longer Human", "Dazai Osamu",
                    120.0, "Fantasy", "1-1-1948")
book2 = AvailEbooks("Before The Coffee Gets Cold",
                    "Toshikazu Kawaguchi", 45.0, "Fantasy & Fiction", "6-12-2015")
book3 = AvailEbooks("Before We Forget Kindness",
                    "Toshikazu Kawaguchi", 49.20, "Fantasy & Fiction", "19-9-2024")
book4 = AvailEbooks("My Story", "Sheikh Mohammed Bin Rashid",
                    21.0, "Autobiography", "15-8-2019")
book5 = AvailEbooks("The Setting Sun", "Dazai Osamu",
                    82.0, "Fiction", "15-12-1947")

# Add each book to the book list
book_list.add_books(book1)
book_list.add_books(book2)
book_list.add_books(book3)
book_list.add_books(book4)
book_list.add_books(book5)

print(book_list.show_selection())  # Display the list of available books

# --- Customer 1: Purchase ---
print("\n--~~ Customer 1: Purchase ~~--")
customer1 = CustInfo("Abdulla Bin Safwan", "202120810@zu.ac.ae",
                     "0509977450", "Abu Dhabi, United Arab Emirates")
print(customer1)  # Display Customer 1's information

# Customer 1's cart and order details
cart1 = CartAndOrder(cust=customer1, orders="2024-09-20", invoiceID="001")
cart1.add_ebook(book1)  # Add book1 to cart
cart1.add_ebook(book3)  # Add book3 to cart
cart1.add_ebook(book4)  # Add book4 to cart
print(cart1)  # Display cart contents for Customer 1

# Generate invoice and display it for Customer 1
payment1 = Invoice(
    order=cart1, transaction_status="Completed", invoiceID="001")
print(payment1)

# Calculate and display total price for Customer 1 without discount
customer1_price = TotalPrice(
    basis_price=120.0 + 49.20 + 21.0, special_cust=False)
print(customer1_price)

# --- Customer 2: Purchase with Discounts ---
print("\n--~~ Customer 2: Purchase with Discounts ~~--")
customer2 = CustInfo("Zayed Mohammed Al Hameli", "ZayedAlHameli@gmail.com",
                     "0504433221", "Abu Dhabi, United Arab Emirates")
print(customer2)

# Customer 2's cart and order details with multiple books
cart2 = CartAndOrder(cust=customer2, orders="2024-10-05", invoiceID="002")
cart2.add_ebook(book1)  # Add book1 to cart
cart2.add_ebook(book2)  # Add book2 to cart
cart2.add_ebook(book3)  # Add book3 to cart
cart2.add_ebook(book4)  # Add book4 to cart
cart2.add_ebook(book5)  # Add book5 to cart
print(cart2)  # Display cart contents for Customer 2

# Generate invoice and display it for Customer 2
payment2 = Invoice(
    order=cart2, transaction_status="Not Yet Paid", invoiceID="002")
print(payment2)

# Calculate and display total price for Customer 2 with discount
customer2_price = TotalPrice(
    basis_price=120.0 + 45.0 + 49.20 + 21.0 + 82.0, special_cust=True)
print(customer2_price)
