from Assignment2 import *  # Import all classes from Assignment2

# Print header for E-Book selection
print("--~~ E-Book Selection Management ~~--")
book_list = List_Of_EBooks()  # Create an instance of the List_Of_EBooks class

# Create instances of AvailEbooks with proper attributes
book1 = AvailEbooks("No Longer Human", "Dazai Osamu", 120.0,
                    "Fantasy", "1-1-1948")  # First book
book2 = AvailEbooks("Before The Coffee Gets Cold", "Toshikazu Kawaguchi",
                    45.0, "Fantasy & Fiction", "6-12-2015")  # Second book
book3 = AvailEbooks("Before We Forget Kindness", "Toshikazu Kawaguchi",
                    49.20, "Fantasy & Fiction", "19-9-2024")  # Third book
book4 = AvailEbooks("My Story", "Sheikh Mohammed Bin Rashid",
                    21.0, "Autobiography", "15-8-2019")  # Fourth book
book5 = AvailEbooks("The Setting Sun", "Dazai Osamu", 82.0,
                    "Fiction", "15-12-1947")  # Fifth book

# Add each book to the book list
book_list.add_books(book1)
book_list.add_books(book2)
book_list.add_books(book3)
book_list.add_books(book4)
book_list.add_books(book5)

print(book_list.show_selection())  # Display the list of available books

# --- Customer 1: Purchase ---
print("\n--~~ Customer 1: Purchase ~~--")  # Print header for Customer 1
customer1 = CustInfo("Abdulla Bin Safwan", "202120810@zu.ac.ae",
                     "0509977450", "Abu Dhabi, United Arab Emirates")  # Create Customer 1
print(customer1)  # Display Customer 1's information

# Customer 1's cart and order details (3 books, no discounts)
# Create cart for Customer 1
cart1 = CartAndOrder(cust=customer1, orders="2024-09-20")
cart1.add_ebook(book1)  # Add book1 to cart
cart1.add_ebook(book2)  # Add book2 to cart
cart1.add_ebook(book3)  # Add book3 to cart
cart1.remove_from_cart(book2)  # Remove book2 from cart
print(cart1)  # Display cart contents for Customer 1

# Generate invoice for Customer 1
payment1 = Invoice(order=cart1, transaction_status="Completed",
                   invoiceID="001")  # Create invoice for Customer 1
print(payment1)  # Display invoice for Customer 1

# Calculate total price for Customer 1 without discount
# Sum of remaining book prices after removing book2
# Create TotalPrice instance for Customer 1
customer1_price = TotalPrice(
    basis_price=120.0 + 49.20 + 21.0, special_cust=False)
# Will show the total price including tax with and without discounts
print(customer1_price)  # Print total price for Customer 1


# --- Customer 2: Purchases with discounts ---
# Print header for Customer 2
print("\n--~~ Customer 2: Purchase with Discounts ~~--")
customer2 = CustInfo("Zayed Mohammed Al Hameli", "ZayedAlHameli@gmail.com",
                     "0504433221", "Abu Dhabi, United Arab Emirates")  # Create Customer 2
print(customer2)  # Display Customer 2's information

# Create cart for Customer 2
cart2 = CartAndOrder(cust=customer2, orders="2024-10-05")
cart2.add_ebook(book1)  # Add book1 to cart
cart2.add_ebook(book2)  # Add book2 to cart
cart2.add_ebook(book3)  # Add book3 to cart
cart2.add_ebook(book4)  # Add book4 to cart
cart2.add_ebook(book5)  # Add book5 to cart
print(cart2)  # Display cart contents for Customer 2

# Generate invoice for Customer 2
payment2 = Invoice(order=cart2, transaction_status="Not Yet Paid",
                   invoiceID="002")  # Create invoice for Customer 2
print(payment2)  # Display invoice for Customer 2

# Calculate total price for Customer 2 with discounts
# Create TotalPrice instance for Customer 2
customer2_price = TotalPrice(
    basis_price=120.0 + 45.0 + 49.20 + 21.0 + 82.0, special_cust=True)
# Will show the total price including tax with and without discounts
print(customer2_price)  # Print total price for Customer 2
