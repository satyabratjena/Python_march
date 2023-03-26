import sqlite3

def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('item.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from item where item_no = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        print("Printing ID ", id)
        for row in records:
            print("item_no  = ", row[0])
            print("item_name  = ", row[1])
            print("item_price  = ", row[2])
            print("item_category  = ", row[3])
            
        else:
            print("no item no found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(12)