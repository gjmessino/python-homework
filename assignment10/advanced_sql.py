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
                        SELECT c.customer_name,
                        AVG(sub.total_price) as total_average_price
                        FROM customers as c
                        LEFT JOIN(
                         SELECT o.customer_id AS customer_id_b,
                         SUM(l.quantity*p.price) AS total_price
                         FROM orders o
                         JOIN line_items l ON o.order_id = l.order_id
                         JOIN products p ON l.product_id = p.product_id
                         )
                        AS sub ON customer_id = sub.customer_id_b
                        GROUP BY o.customer_id
                        """)
        cursor.execute(sql_statement2)
        results = cursor.fetchall()
        for row in results:
            print(row)

## Task 3
        order = []
        sql = ("""SELECT c.customer_id 
               FROM customers c
               WHERE c.customer_name = 'Perez and Sons'""")
        cursor.execute(sql)
        row = cursor.fetchall()
        cust_id = row[0]

        sql2 = ("""SELECT e.employee_id 
                FROM Employees e
                WHERE e.first_name = 'Miranda' AND e.last_name = 'Harris'""")
        cursor.execute(sql2)
        row = cursor.fetchall()
        emp_id = row[0]

        sql3= ("""SELECT p.product_id
               From products p
               ORDER BY p.price ASC
               LIMIT 5""")
        cursor.execute(sql3)
        rows = cursor.fetchall()
        order_ids = []
        for row in rows:
             sql4 = ("""INSERT INTO line_items (product_id,quantity) VALUES (row,5)
                     RETURNING order_id""")
             cursor.execute(sql4)
             order = cursor.fetchall()
             order_ids.append(order)
        sql5 = ("""INSERT INTO orders (order_id,customer_id,emplooyee_id,date) VALUES (order_ids, cust_id, emp_id, '06/08/2026' )""")

## Task 4
        sql_statement3 = ("""SELECT e.first_name, e.last_name, o.order_id
                         FROM employees e      
                         JOIN orders o ON e.employee_id=o.employee_id
                         GROUP BY e.employee_id, e.first_name, e.last_name                   
                         HAVING COUNT(o.order_id) > 5
                         """)
        cursor.execute(sql_statement3)
        results = cursor.fetchall()
        print(results)

except Exception as e:
        print(f'An error occurred: {e}')