from database import get_connection

def verify_customer(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id, name, email, phone, dob, city
        FROM customers
        WHERE customer_id = ?
    """, (customer_id,))

    customer = cursor.fetchone()

    conn.close()

    if customer is None:
        return {
            "success": False,
            "message": "Customer ID not found."
        }

    return {
        "success": True,
        "customer_id": customer[0],
        "name": customer[1],
        "email": customer[2],
        "phone": customer[3],
        "dob": customer[4],
        "city": customer[5]
    }

def get_renewal_details(customer_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT product_name, expiry_date, renewal_amount
        FROM renewals
        WHERE customer_id = ?
        ORDER BY expiry_date
    """, (customer_id,))

    renewals = cursor.fetchall()

    conn.close()

    if not renewals:
        return {
            "success": False,
            "message": "No renewal information found."
        }

    results = []

    for renewal in renewals:

        results.append({
            "product_name": renewal[0],
            "expiry_date": renewal[1],
            "renewal_amount": renewal[2]
        })

    return {
        "success": True,
        "customer_id": customer_id,
        "renewals": results
    }

def search_products(category=None):

    conn = get_connection()
    cursor = conn.cursor()

    if category:

        cursor.execute("""
            SELECT product_id,
                   product_name,
                   category,
                   price,
                   description
            FROM products
            WHERE LOWER(category) = LOWER(?)
        """, (category,))

    else:

        cursor.execute("""
            SELECT product_id,
                   product_name,
                   category,
                   price,
                   description
            FROM products
        """)

    products = cursor.fetchall()

    conn.close()

    results = []

    for product in products:

        results.append({
            "product_id": product[0],
            "product_name": product[1],
            "category": product[2],
            "price": product[3],
            "description": product[4]
        })

    return {
        "success": True,
        "products": results
    }



def create_customer(name, email, phone, dob=None, city=None):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id
        FROM customers
        ORDER BY customer_id DESC
        LIMIT 1
    """)

    last_customer = cursor.fetchone()

    if last_customer:

        last_id = last_customer[0]

        number = int(last_id.replace("CUST", ""))

        new_number = number + 1

    else:

        new_number = 1001

    customer_id = f"CUST{new_number}"

    cursor.execute("""
        INSERT INTO customers
        (customer_id, name, email, phone, dob, city)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        customer_id,
        name,
        email,
        phone,
        dob,
        city
    ))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "customer_id": customer_id,
        "name": name,
        "message": "Customer created successfully."
    }


def save_interest(customer_id, category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interests
        (customer_id, category)
        VALUES (?, ?)
    """, (
        customer_id,
        category
    ))

    conn.commit()
    conn.close()

    return {
        "success": True,
        "customer_id": customer_id,
        "category": category,
        "message": "Interest saved successfully."
    }