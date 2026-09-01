import sqlite3


DB_NAME = "database.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            dob TEXT,
            city TEXT
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS renewals (
            renewal_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,
            product_name TEXT NOT NULL,
            expiry_date TEXT NOT NULL,
            renewal_amount REAL NOT NULL,
            FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id)
        )
    """)


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interests (
            interest_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,
            category TEXT NOT NULL,
            FOREIGN KEY (customer_id)
                REFERENCES customers(customer_id)
        )
    """)

    conn.commit()
    conn.close()


def insert_sample_data():

    conn = get_connection()
    cursor = conn.cursor()




    customers = [
        (
            "CUST1001",
            "Rahul Kumar",
            "rahul@gmail.com",
            "9876543210",
            "1990-05-15",
            "Chennai"
        ),
        (
            "CUST1002",
            "Swetha",
            "swetha@gmail.com",
            "9876543211",
            "1992-08-20",
            "Bangalore"
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO customers
        (customer_id, name, email, phone, dob, city)
        VALUES (?, ?, ?, ?, ?, ?)
    """, customers)




    products = [
        (
            "PROD001",
            "Grocery Package",
            "Grocery",
            1000,
            "Comprehensive grocery package"
        ),
        (
            "PROD002",
            "Electronics Package",
            "Electronics",
            5000,
            "Latest electronic gadgets"
        ),
        (
            "PROD003",
            "Clothing Package",
            "Clothing",
            2000,
            "Fashionable clothing items"
        ),
        (
            "PROD004",
            "Home Appliances",
            "Appliances",
            3000,
            "Essential home appliances"
        ),
        (
            "PROD005",
            "Books and Stationery",
            "Books",
            1500,
            "Educational books and stationery"
        ),
        (
            "PROD006",
            "Sports Equipment",
            "Sports",
            2500,
            "High-quality sports equipment"
        ),
        (
            "PROD007",
            "Toys and Games",
            "Toys",
            1000,
            "Fun toys and games for all ages"
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO products
        (product_id, product_name, category, price, description)
        VALUES (?, ?, ?, ?, ?)
    """, products)



    renewals = [
        (
            "CUST1001",
            "Grocery Package",
            "2026-10-31",
            1000
        ),
        (
            "CUST1002",
            "Electronics Package",
            "2026-11-15",
            5000
        ),
        (
            "CUST1001",
            "Clothing Package",
            "2026-09-28",
            2000
        ),
        (
            "CUST1002",
            "Home Appliances",
            "2026-09-10",
            3000
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO renewals
        (customer_id, product_name, expiry_date, renewal_amount)
        VALUES (?, ?, ?, ?)
    """, renewals)


    conn.commit()
    conn.close()


if __name__ == "__main__":

    create_tables()
    insert_sample_data()

    print("Database created successfully!")