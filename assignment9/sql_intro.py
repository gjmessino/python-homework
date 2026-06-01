import os
import sqlite3

## Task 3 Functions
def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name_pub) VALUES (?)", (name))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")
def add_magazine(cursor, name, pub):
    try:
        cursor.execute("INSERT INTO magazines (name_mag, name_pub) VALUES (?,?)", (name, pub))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")
def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO subscribers (name_subscriber, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")
def add_subscription(cursor, expiration, mag, subscriber):
    try:
        cursor.execute("INSERT INTO subscriptions (expiration, name_mag, name_subscriber) VALUES (?,?,?)", (expiration, mag, subscriber))
    except sqlite3.IntegrityError:
        print("Subsciption is already in the database.")

## Task 1
try:
    with  sqlite3.connect("../db/magazines.db") as conn: 
        cursor = conn.cursor()

## Task 2
        conn.execute("PRAGMA foreign_keys = 1") # This turns on the foreign key constraint
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS publishers (
                    name_pub TEXT PRIMARY KEY,
                    )   
                    """)
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS magazines (
                    name_mag TEXT PRIMARY KEY,
                    name_pub TEXT NOT NULL,
                    FOREIGN KEY (name_pub) REFERENCES publishers (name_pub)
                    )
                    """)
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS subscribers (
                    name_subscriber TEXT,
                    address TEXT NOT NULL
                    CONSTRAINT name_address UNIQUE (name_subscriber, address)

                    )
                    """)
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS subscriptions (
                    expiration TEXT NOT NULL,
                    name_mag TEXT NOT NULL,
                    name_subscriber TEXT NOT NULL,
                    FOREIGN KEY (name_mag) REFERENCES magazines (name_mag),
                    FOREIGN KEY (name_subscriber) REFERENCES subscribers (name_subscriber)
                    )""")
        
    ##Task 3
        add_publisher(cursor,'Vox')
        add_publisher(cursor, 'Conde Naste')
        add_publisher(cursor, 'Hearst')
        add_publisher(cursor, 'Dotdash Meredith')

        add_magazine(cursor, 'Vogue', 'Conde Naste')
        add_magazine(cursor, 'Cosmopolitan', 'Hearst')
        add_magazine(cursor, 'Elle', 'Hearst')
        add_magazine(cursor, 'Womens Health', 'Hearst')

        add_subscriber(cursor, 'Alice', '123 Apple St.')
        add_subscriber(cursor, 'Greg', '456 Banana Ave.')
        add_subscriber(cursor, 'Amanda', '789 Cherry Way')
        add_subscriber(cursor, 'Michael', '1011 Durian Lane')
    
        add_subscription(cursor, '01/11/28', 'Vogue', 'Alice')
        add_subscription(cursor, '12/14/30', 'Elle', 'Alice')
        add_subscription(cursor, '11/4/31', 'People', 'Michael')
        add_subscription(cursor, '04/21/28', 'Womens Health', 'Greg')
        conn.commit() 

    ## Task 4

        cursor.execute("SELECT * FROM subscribers")
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        cursor.execute("SELECT * FROM  magazines ORDER BY name_mag")
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        cursor.execute("""SELECT p.name_pub, m.name_mag 
                    From publishers p 
                    JOIN magazines m 
                    ON p.name_pub = m.name_pub 
                    WHERE p.name_pub='Hearst'""")
        result = cursor.fetchall()
        for row in result:
            print(row)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")