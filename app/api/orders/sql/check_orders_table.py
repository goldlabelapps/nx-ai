"""
Script to check the number of rows in the orders table and print a sample row.
"""
from app.utils.db import get_db_connection_direct

def check_orders_table():
    conn = get_db_connection_direct()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM orders;")
            count = cur.fetchone()[0]
            print(f"orders table row count: {count}")
            if count > 0:
                cur.execute("SELECT * FROM orders LIMIT 1;")
                row = cur.fetchone()
                print("Sample row:")
                print(row)
    print("Check complete.")

if __name__ == "__main__":
    check_orders_table()
