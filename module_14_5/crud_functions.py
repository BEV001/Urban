import sqlite3

db_name = 'database.db'
def initiate_db():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT ,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.close()
    return products

def is_included(user_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?",(user_name,)).fetchone()

    connection.close()
    return check_user is not None

def add_user (user_name, user_email, user_age, user_balance = 1000):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    if is_included(user_name) is False:
        cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)',(user_name, user_email, user_age, user_balance))
    connection.commit()
    connection.close()




"""
def put_products(db_name = 'database.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    for i in range(1,5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                       (f'Товар {i}', f'Описание {i} ', (i * 100)))
    connection.commit()
    connection.close()
"""


if __name__ == '__main__':
     initiate_db()
     #put_products()
     add_user('alice', 'alice@example.com', 30)
     print(is_included('alice'))
     print(is_included('bob'))







