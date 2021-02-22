from book import Book
from database import DataBase


def print_menu():
    print("==== Book Manager ====\n"
          "1) View all books.\n"
          "2) Add a book.\n"
          "3) Edit a book.\n"
          "4) Search for a book.\n"
          "5) Save and exit.\n")


def add_book(cur):
    # Prompt the user for the book title, author and description
    print("Please enter the following information: ")
    title = input("enter book title :")
    author = input("enter book author :")
    description = input("enter book description :");
    book = Book(title, author, description)
    # Save their changes to the database
    book.add_book(cur)
    count = cur.execute("select count(id) from books;")
    print("Book [{}] Saved".format(count.fetchone()[0]))
    return


def book_info(cur, book):
    # method to return the info of the book
    while True:
        x = input("To view details enter the book ID,to return press <Enter>.\nBook Id:")
        if x == "":
            break
        else:
            selected = book.book_info(cur, int(x))
            if selected:
                print("\nID: {}\ntitle: {}\nAuthor: {}\nDescription:{}\n"
                      .format(selected[0], selected[1], selected[2], selected[3]))

    return


def list_all_books(cur):
    #  return all the book from the database
    book = Book
    data = book.list_all_books(cur)
    if len(data):
        for d in data:
            print("[{}] {} .\n".format(d[0], d[1]))
        book_info(cur, book)
    return


def search_book_title(cur):
    title = input("Type in one or more keywords to search for\n Search :")
    book = Book
    data = book.search_book_by_name(cur, title)
    if len(data):
        for d in data:
            print("[{}] {} .\n".format(d[0], d[1]))
        book_info(cur, book)
    return


def load_books(cur):
    # load the book at the first of the program return the count
    count = cur.execute("select count(id) from books;")
    print("Loaded [{}] books into the library.".format(count.fetchone()[0]))
    return


def edit_book(cur):
    #  edit the selected book
    book = Book
    data = book.list_all_books(cur)
    #  create temp dict to hold the info of the selected book to detect the changes
    temp = {}
    for d in data:
        print("[{}] {} .\n".format(d[0], d[1]))
    while True:
        id = input("Enter the book ID of the book you want to edit; to return press <Enter>.\n Book ID: ")
        if id != "":
            seleted_book = book.book_info(cur, int(id))
            if seleted_book:
                #  make the update operation on the selected book
                temp['id'] = seleted_book[0]

                t = input("Title [{}]:".format(seleted_book[1]))
                if t != "":
                    temp['title'] = t
                else:
                    temp['title'] = seleted_book[1]

                a = input("Author [{}]:".format(seleted_book[2]))
                if a != "":
                    temp['Author'] = a
                else:
                    temp['Author'] = seleted_book[2]

                d = input("Description [{}]:".format(seleted_book[3]))
                if t != "":
                    temp['Description'] = d
                else:
                    temp['Description'] = seleted_book[3]
                #  call the update method to update it into the database
                book.update_book(cur, temp['id'], temp['title'], temp['Author'], temp['Description'])
                print("Book saved.")
        else:
            return


def menu():
    try:
        # establish the connection to the database
        connection = DataBase.create_connection('bookDB.sqlite')
        cur = connection.cursor()
        # the count of the book in the db
        load_books(cur)
        while True:
            print_menu()
            res = input("Choose [1-5]:")
            if res == "1":
                print("==== View books ====\n")
                # list books
                list_all_books(cur)
            elif res == "2":
                print("==== Add a book ====\n")
                add_book(cur)
            elif res == "3":
                print("==== Edit a book ====\n")
                edit_book(cur)
            elif res == "4":
                print("==== Search for a book ====\n")
                search_book_title(cur)
            elif res == "5":
                #  after closing the app commit the transactions into db and close the connection
                print("Library saved.\n")
                connection.commit()
                connection.close()
                break

    except Exception as e:
        print(e)


if __name__ == "__main__":
    menu()
