import sqlite3

def insertVaribleIntoTable(task_id, task_name, task_priority):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO task
                          (task_id, task_name, task_priority)
                           VALUES 
                          (?,?,?)"""

        data_tuple = (task_id, task_name, task_priority)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable(1, 'python', "high")