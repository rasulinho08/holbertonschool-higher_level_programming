#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)
    cursor = db.cursor()
    
    # Execute SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    
    # Fetch all results and print them
    for state in cursor.fetchall():
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()

