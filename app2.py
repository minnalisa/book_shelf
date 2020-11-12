import  database2

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 's' to search a book
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """ 

def add_book():
    user_book = input("Enter the name of the book, author, year:\n")

    try:
        book, author, year = user_book.split(",")
        
    except ValueError:
        print("Enter name of book, author, year seperate with ',' ")
        add_book()
    else:   
        database.add_db(
            book.strip().capitalize(),
            author.strip().capitalize(),
            year.strip()
            )
        print(f"Added '{book}' {author} {year} to the book store.")
  
    
def list_book():
    print("List of BOOKS from database:")
    for book in database.retrive_db():
        print_format(book)


def search_book():
    search_input = input("Enter book name or author or year:\n").strip().capitalize()
    found_book = [print_format(book) for book in database._check_book(search_input)]
    if not found_book:
        print(f"'{search_input}' doesn't match with any book entry.")
       
    
def print_format(book):
    read = "Yes" if book["READ"] else "No"
    print( f""" 
    BOOK: {book["BOOK"]}
    AUTHOR: {book["AUTHOR"]}
    YEAR: {book["YEAR"]}
    READ: {read} """)


def mark_read():
    mark_read_input = input("Enter the book to mark as 'read':\n").capitalize()
    print(database.mark_db(mark_read_input))
    

def delete_book():
    del_input = input("Enter the book to remove:\n").strip().capitalize()
    print(database.delete_db(del_input))
    

menu_list = {
    'a': add_book,
    'l': list_book,
    's': search_book,
    'r': mark_read,
    'd': delete_book
}

def menu_user():
    database.initiate_db()
    user_menu = input(USER_CHOICE)
    while True:
        if user_menu in menu_list:
            menu_select = menu_list[user_menu]
            menu_select()
        
        elif user_menu == 'q':
            print("Good Bye...XX")
            database.connection.close()
            break

        else:
            print(f"Menu '{user_menu}' does not exist..")
        user_menu = input(USER_CHOICE)

menu_user()
