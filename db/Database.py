import sqlite3
from utils.Constants import *

conn = sqlite3.connect("Note.db",check_same_thread=False)
cursor = conn.cursor()


class Database:
    def __init__(self) -> None:

        try:
            # cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
            cursor.execute(f"""CREATE TABLE {TABLE_NAME}(
                            id INTEGER PRIMARY KEY,
                            {COLUMN_NAME_TITLE} TEXT,
                            {COLUMN_NAME_DESCRIPTION} TEXT
                            )""")

            conn.commit()

        except Exception as e:
            pass


    def readAll(self):
        try:
            cursor.execute(f""" SELECT * FROM {TABLE_NAME}""")
            rows  = cursor.fetchall()
            return rows
        except Exception as e:
            print("Exception in readAll")
            print(e)
            conn.rollback()
 



    def readOne(self, noteId):
        try:
            cursor.execute(f""" SELECT * FROM {TABLE_NAME} WHERE id == {noteId}""")
            row = cursor.fetchone()
            return row
        except Exception as e:
            print("Exception in readOne")
            print(e)
            conn.rollback()



    def create(self, title, des):
        try:
            cursor.execute(f""" INSERT INTO {TABLE_NAME} ({COLUMN_NAME_TITLE}, {COLUMN_NAME_DESCRIPTION}) VALUES( ?, ?)""",(title, des,))
            conn.commit()
        except Exception as e:
            print("Exception in create")
            print(e)
            conn.rollback()



    def update(self, noteId, title, des):
        try:
            cursor.execute(f""" UPDATE {TABLE_NAME} SET {COLUMN_NAME_TITLE} = ?, {COLUMN_NAME_DESCRIPTION} = ? WHERE id == ?""", (title, des, noteId,))
            conn.commit()
        except Exception as e:
            print("Exception in update")
            print(e)
            conn.rollback()



    def delete(self, noteId):
        try:
            cursor.execute(f""" DELETE FROM {TABLE_NAME} WHERE id == {noteId}""")
            conn.commit()
        except Exception as e:
            print("Exception in delete")
            print(e)
            conn.rollback()
