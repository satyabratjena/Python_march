import sqlite3

def insertVaribleIntoTable(item_no,item_name,item_price,item_category):
    try:
        sqliteConnection = sqlite3.connect('item.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO item
                          (item_no,item_name,item_price,item_category)
                           VALUES 
                          (?,?,?,?)"""

        data_tuple = (item_no,item_name,item_price,item_category)
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

insertVaribleIntoTable(12, 'brush', 345.00, "necessary")