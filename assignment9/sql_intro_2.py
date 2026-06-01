import os
import sqlite3
import pandas as pd

## Task 5
try:
    with  sqlite3.connect("../db/lesson.db") as conn: 
        cursor = conn.cursor()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")