import sqlite3
import os 


def setup_db():
    if os.path.exists("database.sqlite3"):
        print("Database.sqlite3 exists!")

    else:
        print("Database.sqlite3 does not exist.\nSetting up database.")
        
        with sqlite3.connect("database.sqlite3") as conn:
          cursor = conn.cursor()
          cursor.execute("""CREATE TABLE comments (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          title TEXT,
                          full_name TEXT,
                          text_comment TEXT
                          )""")


def load_all_from_db():
  with sqlite3.connect("database.sqlite3") as conn:
    cursor = conn.cursor()
    result = cursor.execute("""SELECT id, title, full_name, text_comment FROM comments""")
    return [dict(zip(["id", "title", "full_name", "text_comment"], row)) for row in result]


def load_three_from_db():
  with sqlite3.connect("database.sqlite3") as conn: 
    cursor = conn.cursor()
    result = cursor.execute("""SELECT id, title, full_name, text_comment FROM comments ORDER BY id DESC LIMIT 3""")
    return [dict(zip(["id", "title", "full_name", "text_comment"], row)) for row in result]


def load_id_from_db(id):
  with sqlite3.connect("database.sqlite3") as conn:
    cursor = conn.cursor()
    result = cursor.execute("""SELECT * FROM comments WHERE id = ?""",
                          (id,))
    row = result.fetchall()

    if len(row) == 0:
      return None
    
    else:
      row_dict = {}
      row_dict["id"] = row[0][0]
      row_dict["title"] = row[0][1]
      row_dict["full_name"] = row[0][2]
      row_dict["text_comment"] = row[0][3]
      return row_dict
    

def add_comment_to_db(data):
  with sqlite3.connect("database.sqlite3") as conn:
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO comments (title, full_name, text_comment) VALUES (?, ?, ?)""",
                  (data["title"], data["full_name"], data["text_comment"]))