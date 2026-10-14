# SIMPLE LIBRARY MANAGEMENT SYSTEM
# No libraries needed. Just two lists!

books = []      # books available in the library
issued = []     # books that are given out

while True:
    print("\n--- LIBRARY MENU ---")
    print("1. Add a book")
    print("2. Show books")
    print("3. Issue a book")
    print("4. Return a book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        books.append(name)
        print("Book added!")

    elif choice == "2":
        print("Available books:", books)
        print("Issued books:", issued)

    elif choice == "3":
        name = input("Enter book name to issue: ")
        if name in books:
            books.remove(name)
            issued.append(name)
            print("Book issued!")
        else:
            print("Book not available.")

    elif choice == "4":
        name = input("Enter book name to return: ")
        if name in issued:
            issued.remove(name)
            books.append(name)
            print("Book returned!")
        else:
            print("This book was not issued.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong choice, try again.")