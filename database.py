import json

book_in = ""
book_db = []

def add_db(book, author = "UNKNOWN", year = "UNKNOWN"):
    global book_in
    book_in = {
        "BOOK": book,
        "AUTHOR": author,
        "YEAR": year,
        "READ" : False
    }
    
def retrive_db():
        try:
            with open("book_database_json.txt", 'r') as books:
                book_info = json.load(books)
        except (json.JSONDecodeError, FileNotFoundError):
            return [{"BOOK": 0, "AUTHOR": 0, "YEAR": 0, "READ": 0}]
        else:
            return book_info

  
def mark_db(book):
    global book_db
    book_db = retrive_db()
    for book_info in book_db:
        if book_info['BOOK'] ==  book:
            book_info['READ'] = True
            book_db
            return f"{book} is marked as 'Read'."
    else:
        return f"Book '{book}'' doesn't exist in Book Store"


def delete_db(book):
    global book_db
    book_db = retrive_db()
    for book_info in book_db:
        if book_info['BOOK'] ==  book:
            book_db.remove(book_info)
            if len(book_db) == 0:
                file = open("book_database_json.txt", "r+")
                file.truncate(0)
                file.close()
            return f"{book} is removed"
    else:
        return f"BOOK: '{book}' doesn't exist in Book Store."
        

def save_to_db():
    global book_in
    global book_db
    if book_in:
        try: 
            with open('book_database_json.txt', '+r') as file:
                data = json.load(file)
                data.append(book_in)
                file.seek(0)
                json.dump(data, file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open('book_database_json.txt', 'w') as file:
                initiate_db = []
                initiate_db.append(book_in)
                json.dump(initiate_db, file) 
        book_in = ""
    
    elif book_db:
        with open('book_database_json.txt', 'w') as file:
            json.dump(book_db, file)
        book_db = []
   


    

        
        
    

