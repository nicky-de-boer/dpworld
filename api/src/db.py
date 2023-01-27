import sqlite3


def connect_to_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    sqlite_insert_query = """INSERT or REPLACE INTO nicky
                              (date, score) 
                               VALUES 
                              ('2022-10-16',21158)"""
    cursor.execute("SELECT * FROM nicky")

    count = cursor.execute(sqlite_insert_query)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
    return conn


def create_db_table():
    try:

        # for item in ['martijn', 'nicky', 'david']:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE nicky (
                date DATE PRIMARY KEY NOT NULL,
                score INTEGER NOT NULL
            );
        ''')
        # conn.execute('''
        #             CREATE TABLE martijn (
        #                 user_id INTEGER PRIMARY KEY NOT NULL,
        #                 name TEXT NOT NULL,
        #                 email TEXT NOT NULL,
        #                 phone TEXT NOT NULL,
        #                 address TEXT NOT NULL,
        #                 country TEXT NOT NULL
        #             );
        #         ''')
        # conn.execute('''
        #             CREATE TABLE martijn (
        #                 user_id INTEGER PRIMARY KEY NOT NULL,
        #                 name TEXT NOT NULL,
        #                 email TEXT NOT NULL,
        #                 phone TEXT NOT NULL,
        #                 address TEXT NOT NULL,
        #                 country TEXT NOT NULL
        #             );
        #         ''')
        conn.commit()
    except:
        print("user table creation failed")
    finally:
        conn.close()


if __name__ == "__main__":
    connect_to_db()
