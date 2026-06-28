import sqlite3
#import inquirer

connection = sqlite3.connect("database.db")


try:
    cursor = connection.cursor()

    # 3. Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            completed BOOL,
            priority INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completed_tasks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            completed BOOL,
            priority INTEGER
        )
    """)


except sqlite3.Error as error:
    print(f"Database error occurred: {error}")

finally:
    # 10. Always close the connection when finished
    connection.commit()
    connection.close()