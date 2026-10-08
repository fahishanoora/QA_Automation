import sqlite3

def test_database_user_validation():
    # 1. Connect to an in-memory test database
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    
    # 2. Create a 'users' table inside the database
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            role TEXT
        )
    """)
    
    # 3. INSERT a user (Simulating data created by our app)
    cursor.execute("INSERT INTO users VALUES (1, 'fahisha_qa', 'SDET Lead')")
    connection.commit()
    
    # 4. SELECT query to fetch and validate the user record
    cursor.execute("SELECT username, role FROM users WHERE id = 1")
    user_record = cursor.fetchone()  # Fetches ('fahisha_qa', 'SDET Lead')
    
    # 5. Assert database values match expectations!
    assert user_record[0] == "fahisha_qa"
    assert user_record[1] == "SDET Lead"
    
    # Close connection
    connection.close()


def test_user_orders_join_validation():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE users (id INT, name TEXT)")
    cursor.execute("CREATE TABLE orders (id INT, user_id INT, item TEXT, amount REAL)")

    cursor.execute("INSERT INTO users VALUES (101, 'Fahisha')")
    cursor.execute("INSERT INTO orders VALUES (5001, 101, 'Mechanical Keyboard', 89.99)")
    connection.commit()

    query = """
        SELECT users.name, orders.item, orders.amount
        FROM orders
        INNER JOIN users ON orders.user_id = users.id
        WHERE users.id = 101
    """
    cursor.execute(query)
    record = cursor.fetchone()

    assert record[0] == "Fahisha"
    assert record[1] == "Mechanical Keyboard"
    assert record[2] == 89.99


    connection.close()