import sqlite3

def create_database():
    conn=sqlite3.connect('books.db')
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tittle TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL
            )
        ''')
    
    cursor.executemany('''
            INSERT INTO books(tittle,author,price)
            VALUES (?,?,?)
            ''',[
                ('Book One' , 'Author A',9.99),
                ('Book Two' , 'Author B',14.99),
                ('Book Three' , 'Author C',7.99)
            ])
    
    conn.commit()
    conn.close()
    
create_database()