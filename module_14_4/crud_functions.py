import sqlite3

def intiate_bd(db_name = 'database.db'):
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
    connection.commit()
    connection.close()

def get_all_products(db_name = 'database.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.close()
    return products


def put_products(db_name = 'database.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    for i in range(1,5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES(?, ?, ?)",
                       (f'Товар {i}', f'Описание {i} ', (i * 100)))
    connection.commit()
    connection.close()


if __name__ == '__main__':
     intiate_bd(db_name='database.db')
     put_products(db_name='database.db')







