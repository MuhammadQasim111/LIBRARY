books = [
    {"id": 1, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy", "availability": "Available"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "availability": "Available"},
  
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": []},
  
]

def search_books(query):
    results = []
    for book in books:
        if query.lower() in book["title"].lower() or query.lower() in book["author"].lower() or query.lower() in book["genre"].lower():
            results.append(book)
    return   results

def borrow_book(user_id, book_id):
    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)

    if user and book and book["availability"] == "Available":
        user["borrowed_books"].append(book)
        book["availability"] = "Checked Out"
        print(f"You have borrowed '{book['title']}'")
    else:
        print("Book not available or user not found.")

def return_book(user_id, book_id):
    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)

    if user and book and book["availability"] == "Checked Out":
        user["borrowed_books"].remove(book)
        book["availability"] = "Available"
        print(f"You have returned '{book['title']}'")
    else:
        print("Book not checked out or user not found.")

def view_all_books():
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Availability: {book['availability']}")

def view_available_books():
    for book in books:
        if book["availability"] == "Available":
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

def view_checked_out_books():
    for book in books:
        if book["availability"] == "Checked Out":
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Search Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. View Available Books")
        print("6. View Checked-Out Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter search query: ")
            results = search_books(query)
            if results:
                for book in results:
                    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Availability: {book['availability']}")
            else:
                print("No books found.")
        elif choice == "2":
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter the book ID to borrow: "))
            borrow_book(user_id, book_id)
        elif choice == "3":
            user_id = int(input("Enter your user ID: "))
            book_id = int(input("Enter the book ID to return: "))
            return_book(user_id, book_id)
        elif choice == "4":
            view_all_books()
        elif choice == "5":
            view_available_books()
        elif choice == "6":
            view_checked_out_books()
        elif choice == "7":
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  
    
    






