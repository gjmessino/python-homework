import csv
import sqlite3
import pandas as pd

## Task 5
try:
    with  sqlite3.connect("../db/lesson.db") as conn: 
        cursor = conn.cursor()
        sql_statement = ("""SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price 
                        FROM line_items l 
                        JOIN products p 
                        ON l.product_id = p.product_id;""")
        df = pd.read_sql_query(sql_statement, conn)
        print(df.head(5))
        
        df['total'] = df['quantity'] * df['price']
        print(df.head(5))

        df_group = df.groupby('product_id').agg({'line_item_id' : 'count',
                                                 'total' : 'sum',
                                                 'product_name' : 'first'
                                                 })
        print(df_group.head(5))

        df_group = df_group.sort_values(by='product_name')
        df_group.to_csv('./order_summary.csv')

except sqlite3.Error as e:
    print(f"An error occurred:")