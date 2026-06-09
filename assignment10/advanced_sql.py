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
        conn.commit()

## Task 2
        sql_statement2 =("""
                        SELECT c.customer_name,
                        AVG(sub.total_price) as total_average_price
                        FROM customers as c
                        LEFT JOIN(
                         SELECT o.customer_id AS customer_id_b,
                         SUM(l.quantity*p.price) AS total_price
                         FROM orders o
                         JOIN line_items l ON o.order_id = l.order_id
                         JOIN products p ON l.product_id = p.product_id
                         GROUP BY o.customer_id
                         )
                        AS sub ON c.customer_id = sub.customer_id_b
                        GROUP BY c.customer_id, c.customer_name; 
                        """)
        cursor.execute(sql_statement2)
        results = cursor.fetchall()
        for row in results:
            print(row)
        conn.commit()

## Task 3
        order = []
        sql = ("""SELECT c.customer_id 
               FROM customers c
               WHERE c.customer_name = 'Perez and Sons'""")
        cursor.execute(sql)
        cust_id = cursor.fetchone()[0]

        sql2 = ("""SELECT e.employee_id 
                FROM Employees e
                WHERE e.first_name = 'Miranda' AND e.last_name = 'Harris'""")
        cursor.execute(sql2)
        emp_id = cursor.fetchone()[0]

        sql3= ("""SELECT p.product_id
               From products p
               ORDER BY p.price ASC
               LIMIT 5""")
        cursor.execute(sql3)
        rows = cursor.fetchall()

        conn.execute('PRAGMA foreign_keys = 1')
        sql4 = ("""INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, '2026-06-08') RETURNING order_id""")
        cursor.execute(sql4, (cust_id, emp_id))
        new_order_id = cursor.fetchone()[0]

        conn.execute('PRAGMA foreign_keys = 1')
        sql5 = ("""INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, 10)""")
        for row in rows:
             prod_id = row[0]
             cursor.execute(sql5, (new_order_id, prod_id))
             
        sql6 = ("""
                SELECT l.line_item_id, l.quantity, p.product_name
                FROM line_items l
                JOIN products p ON l.product_id = p.product_id
                WHERE l.order_id = ?
                """)
        cursor.execute(sql6,(new_order_id))
        results = cursor.fetchall()
        for row in results:
              print(row)
        
        conn.commit()

# Task 4
        sql_statement3 = ("""
                          SELECT e.first_name, e.last_name, e.employee_id
                          COUNT(o.order_id) AS order_count
                          FROM employees e      
                          JOIN orders o ON e.employee_id=o.employee_id
                          GROUP BY e.employee_id, e.first_name, e.last_name                  
                          HAVING COUNT(o.order_id) > 5
                         """)
        cursor.execute(sql_statement3)
        results = cursor.fetchall()
        print(results)

        conn.commit()
except Exception as e:
        conn.rollback()
        print(f'An error occurred: {e}')