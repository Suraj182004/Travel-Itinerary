import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('travel_itinerary.db')
cursor = conn.cursor()

def print_table_info(table_name):
    print(f"\n==== TABLE: {table_name} ====")
    
    # Get column information
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print("Columns:")
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
    
    # Get row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"\nRow count: {count}")
    
    # Get sample data (first 3 rows)
    if count > 0:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
        rows = cursor.fetchall()
        print("\nSample data (first 3 rows):")
        for row in rows:
            print(f"  {row}")

# Get list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Available tables in the database:")
for table in tables:
    table_name = table[0]
    print(f"- {table_name}")
    print_table_info(table_name)

conn.close() 