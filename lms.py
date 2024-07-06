import sqlite3

con = sqlite3.connect("LMS.db")
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

def view_books():
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()
    for row in data:
        # print(row)
        print("Book Name: {0}".format(row[1]))

def get_books():
    book_name = input("Enter Book name: ")
    cur.execute('''DELETE FROM Books WHERE name = ?''', (book_name,))
    con.commit()

def add_books():
    name = input("Enter book name: ")
    cur.execute('''INSERT INTO books (name) VALUES (?)''',(name,))
    con.commit()

def main():
    while True:
        print("`````````Library Management System`````````")
        print('''Select one option
        1. View Books
        2. Get Books
        3. Add Books
        4. Exist''')
        op = int(input("Enter here: "))
        match op:
            case 1:
                view_books()
            case 2:
                get_books()
            case 3:
                add_books()
            case 4:
                break
            case _:
                print("Invalid Option!")
        print("")
    con.close()
if __name__ == "__main__":
    main()