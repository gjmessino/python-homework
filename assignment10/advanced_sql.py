import sqlite3

try:
    with  sqlite3.connect("../db/lesson.db") as conn: 
        cursor = conn.cursor()
## Task 1
        sql_statement =("""
                        SELECT o.order_id,
                        SUM(l.quantity*p.price) AS total
                        FROM orders o
                        JOIN line_items l ON o.order_id = l.order_id
                        JOIN products p ON l.product_id = p.product_id
                        GROUP BY o.order_id
                        ORDER BY o.order_id LIMIT 5
                        """)
        cursor.execute(sql_statement)
        results = cursor.fetchall()
        print(results)

## Task 2
        sql_statement2 =("""
                        SELECT c.customer_id,
                        AVG(sub.total_price) as total_average_price
                        FROM customers as c
                        LEFT JOIN(
                         SELECT o.customer_id AS customer_id_b,
                         SUM(l.quantity*p.price) AS total_price
                         FROM orders o
                         JOIN line_items l ON o.order_id = l.order_id
                         JOIN products p ON l.product_id = p.product_id
                         GROUP BY o.order_id)
                        AS  sub ON c.customer_id = sub.customer_id_b
                        """)
        cursor.execute(sql_statement2)
        results = cursor.fetchall()
        for row in results:
            print(results)

## Task 3
        sql_statement3 = ("""
                          SELECT c.customer_id 
                          FROM customers c
                          WHERE c.customer_name = 'Perez and Sons'
                          SELECT e.employee_id 
                          FROM Employees e
                          WHERE e.first_name = 'Miranda' AND e.last_name = 'Harris'
                          SELECT p.product_id
                          HAVING MIN(p.price) LIMIT 5
""")
        
        cursor.execute("INSERT INTO orders (order_id, customer_id, employee_id) VALUES ()")
    print(f'An error occurred: {e}')