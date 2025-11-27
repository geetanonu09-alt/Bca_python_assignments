import csv
import os

# ------------------------------------
# Data Structures
# ------------------------------------
books = {}      # book_id → {"title":..., "author":..., "copies":...}
borrowed = {}   # student_name → list of book_ids
student_names = set()    # demonstration of sets


# ------------------------------------
# Helper Function
# ------------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------
# Add / Update Book
# ------------------------------------
def add_book():
    print("\n--- Add / Update Book ---")
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    try:
        copies = int(input("Enter number of copies: "))
        if copies < 0:
            raise ValueError
    except ValueError:
        print("Invalid number of copies.")
        return

    if book_id in books:
        books[book_id]["copies"] += copies
        print(f"Copies updated. Total: {books[book_id]['copies']}")
    else:
        books[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"Book {book_id} added successfully.")


# ------------------------------------
# View Books
# ------------------------------------
def view_books():
    print("\n--- Library Books ---")
    if not books:
        print("No books available.")
        return

    print(f"{'Book ID':<8} {'Title':<25} {'Author':<20} {'Copies':<6}")
    print("-" * 65)

    for bid, info in books.items():
        print(f"{bid:<8} {info['title']:<25} {info['author']:<20} {info['copies']:<6}")

    print("-" * 65)


# ------------------------------------
# Search Book
# ------------------------------------
def search_book():
    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title keyword")
    choice = input("Enter choice: ")

    if choice == "1":
        bid = input("Enter Book ID: ").strip()
        info = books.get(bid)
        if info:
            print(f"Found: {bid} → {info}")
        else:
            print("Book ID not found.")

    elif choice == "2":
        keyword = input("Enter keyword: ").lower()
        results = [(bid, info) for bid, info in books.items()
                   if keyword in info['title'].lower()]

        if results:
            print(f"\nFound {len(results)} book(s):")
            for bid, info in results:
                print(f"{bid}: {info['title']} by {info['author']} (Copies: {info['copies']})")
        else:
            print("No matching titles found.")
    else:
        print("Invalid choice.")


# ------------------------------------
# Borrow Book
# ------------------------------------
def borrow_book():
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ").strip()
    book_id = input("Enter Book ID: ").strip()

    if book_id not in books:
        print("Book does not exist.")
        return

    if books[book_id]["copies"] <= 0:
        print("No copies available.")
        return

    books[book_id]["copies"] -= 1
    borrowed.setdefault(student, []).append(book_id)
    student_names.add(student)

    print(f"{student} borrowed {book_id} successfully.")


# ------------------------------------
# Return Book
# ------------------------------------
def return_book():
    print("\n--- Return Book ---")
    student = input("Enter Student Name: ").strip()

    if student not in borrowed or not borrowed[student]:
        print("No borrowing record found.")
        return

    print(f"Borrowed books: {borrowed[student]}")
    book_id = input("Enter Book ID to return: ").strip()

    if book_id not in borrowed[student]:
        print("Invalid return.")
        return

    borrowed[student].remove(book_id)
    books[book_id]["copies"] += 1

    print(f"{student} returned {book_id} successfully.")

    # list comprehension
    borrowed_list = [f"{stu} -> {', '.join(bks)}"
                     for stu, bks in borrowed.items() if bks]
    print("\nUpdated Borrowed List:")
    for line in borrowed_list:
        print(line)


# ------------------------------------
# View Borrowed Records
# ------------------------------------
def view_borrowed():
    print("\n--- Borrowed Records ---")
    if not borrowed or all(len(v) == 0 for v in borrowed.values()):
        print("No borrowed books.")
        return

    for student, books_list in borrowed.items():
        if books_list:
            print(f"{student} -> {', '.join(books_list)}")


# ------------------------------------
# Bonus Features
# ------------------------------------
def save_books_csv():
    with open("books.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["book_id", "title", "author", "copies"])
        for bid, info in books.items():
            writer.writerow([bid, info["title"], info["author"], info["copies"]])
    print("Books saved to books.csv")


def load_books_csv():
    if not os.path.exists("books.csv"):
        print("books.csv not found.")
        return
    with open("books.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        books.clear()
        for row in reader:
            books[row["book_id"]] = {
                "title": row["title"],
                "author": row["author"],
                "copies": int(row["copies"])
            }
    print("Books loaded from books.csv")


# ------------------------------------
# Menu
# ------------------------------------
def show_menu():
    print("\n" + "=" * 55)
    print("          Library Book Manager CLI")
    print("=" * 55)
    print("1. Add / Update Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Borrowed Records")
    print("7. Save to CSV")
    print("8. Load from CSV")
    print("0. Exit")


def main():
    clear_screen()
    print("Welcome to Library Manager CLI\n")

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            view_borrowed()
        elif choice == "7":
            save_books_csv()
        elif choice == "8":
            load_books_csv()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to continue...")
        clear_screen()


if __name__ == "__main__":
    main()
